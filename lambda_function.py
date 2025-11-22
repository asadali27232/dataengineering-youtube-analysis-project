import boto3
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import urllib.parse
import os
import io
import json

s3 = boto3.client("s3")
glue = boto3.client("glue")

CLEANSING_PATH = os.environ['s3_cleansed_layer']
GLUE_DB = os.environ['glue_catalog_db_name']
GLUE_TABLE = os.environ['glue_catalog_table_name']
WRITE_MODE = os.environ['write_data_operation']


def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    try:
        obj = s3.get_object(Bucket=bucket, Key=key)
        json_bytes = obj["Body"].read()
        df_raw = pd.read_json(io.BytesIO(json_bytes))

        df = pd.json_normalize(df_raw["items"])

        table = pa.Table.from_pandas(df)

        output_key = _determine_parquet_key()

        # Write Parquet to S3
        buf = io.BytesIO()
        pq.write_table(table, buf)
        buf.seek(0)

        s3.upload_fileobj(buf,
                          CLEANSING_PATH.replace("s3://", "").split("/")[0],
                          output_key)

        _ensure_glue_table(df)

        return {
            "status": "success",
            "output_key": output_key
        }

    except Exception as e:
        print(e)
        raise e


def _determine_parquet_key():
    """Exactly matches what awswrangler does internally."""
    import uuid
    file_name = f"{uuid.uuid4()}.parquet"

    path = CLEANSING_PATH.replace("s3://", "")
    parts = path.split("/", 1)

    bucket = parts[0]
    prefix = parts[1] if len(parts) > 1 else ""

    if prefix.endswith("/"):
        final = prefix + file_name
    else:
        final = prefix + "/" + file_name

    return final


def _ensure_glue_table(df: pd.DataFrame):

    # 1) Convert DF schema → Glue schema
    cols = []
    for col, dtype in df.dtypes.items():
        glue_type = _map_dtype(str(dtype))
        cols.append({"Name": col, "Type": glue_type})

    # 2) Try to get existing table
    try:
        glue.get_table(DatabaseName=GLUE_DB, Name=GLUE_TABLE)
        table_exists = True
    except glue.exceptions.EntityNotFoundException:
        table_exists = False

    bucket, prefix = _split_s3_path(CLEANSING_PATH)

    storage_descriptor = {
        "Columns": cols,
        "Location": CLEANSING_PATH,
        "InputFormat": "org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat",
        "OutputFormat": "org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat",
        "SerdeInfo": {
            "SerializationLibrary": "org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe",
            "Parameters": {"serialization.format": "1"}
        }
    }

    if not table_exists:
        glue.create_table(
            DatabaseName=GLUE_DB,
            TableInput={
                "Name": GLUE_TABLE,
                "TableType": "EXTERNAL_TABLE",
                "Parameters": {"classification": "parquet"},
                "StorageDescriptor": storage_descriptor
            }
        )
    else:
        glue.update_table(
            DatabaseName=GLUE_DB,
            TableInput={
                "Name": GLUE_TABLE,
                "TableType": "EXTERNAL_TABLE",
                "Parameters": {"classification": "parquet"},
                "StorageDescriptor": storage_descriptor
            }
        )


def _map_dtype(dtype: str):
    if "int" in dtype:
        return "int"
    if "float" in dtype:
        return "double"
    if "bool" in dtype:
        return "boolean"
    return "string"


def _split_s3_path(path):
    path = path.replace("s3://", "")
    parts = path.split("/", 1)
    bucket = parts[0]
    prefix = parts[1] if len(parts) > 1 else ""
    return bucket, prefix
