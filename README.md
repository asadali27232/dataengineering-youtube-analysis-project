# YouTube's Data Engineering: ETL & Cloud Pipeline Project

---

## Overview

This project aims to securely manage, streamline, and perform analysis on structured and semi-structured YouTube videos data. The analysis focuses on video categories, trending metrics, and engagement statistics.

The system is designed to be **scalable, cloud-based, and interactive**, allowing users to generate insights from large datasets efficiently.

---

## Project Goals

1. **Data Ingestion**  
   Build mechanisms to ingest data from multiple sources securely and efficiently.

2. **ETL System**  
   Transform raw YouTube data into a structured format suitable for analysis and reporting.

3. **Data Lake**  
   Centralize data from multiple sources into a single repository for better accessibility and management.

4. **Scalability**  
   Ensure the system scales with increasing data volumes without performance bottlenecks.

5. **Cloud Integration**  
   Process large-scale data in the cloud using AWS services instead of relying on local machines.

6. **Reporting & Visualization**  
   Build interactive dashboards to generate insights and answer analytical questions using **Power BI**.

---

## AWS Services Used

| Service                                                                                                                 | Purpose                                                                     |
| ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| ![Amazon S3](https://img.shields.io/badge/Amazon%20S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white)         | Object storage service for scalable, secure, and available data storage.    |
| ![AWS IAM](https://img.shields.io/badge/AWS%20IAM-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)           | Manage access and permissions to AWS resources securely.                    |
| ![AWS Glue](https://img.shields.io/badge/AWS%20Glue-232F3E?style=for-the-badge&logo=aws-glue&logoColor=white)           | Serverless data integration for discovery, transformation, and preparation. |
| ![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-FF9900?style=for-the-badge&logo=aws-lambda&logoColor=white)     | Run code without managing servers, used for automation tasks.               |
| ![AWS Athena](https://img.shields.io/badge/AWS%20Athena-4B0082?style=for-the-badge&logo=aws-athena&logoColor=white)     | Interactive querying service for data stored in S3 using SQL.               |
| ![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=microsoft-power-bi&logoColor=black) | Used to visualize data through an interactive dashboard.                    |

## Dataset Used

-   **Source:** [Kaggle - Trending YouTube Videos Dataset](https://www.kaggle.com/datasets/datasnaek/youtube-new)
-   **Description:**  
    The dataset contains statistics (CSV files) on daily trending YouTube videos across multiple regions.  
    Each file contains up to 200 trending videos per day and includes the following fields:

    -   `video_id`, `title`, `channel_title`, `publish_time`, `tags`, `views`, `likes`, `dislikes`, `description`, `comment_count`
    -   `category_id` linked via JSON files for each region

-   **Data Type:** Structured CSV files and JSON for category mapping.

---

## Architecture Diagram

![Architecture Diagram](static/architecture.jpeg)

## Folders & Files

-   **`aws_cli_commands.sh`** – AWS CLI commands for S3 bucket (IAM usr configured on aws cli).
-   **`fetch_athena.ipynb`** – Queries Athena and generates **`final_yt_data.csv`** for analysis.
-   **`final_yt_data.csv`** – Cleaned dataset used for analysis and dashboard.
-   **`dashboard.pbix`** – Power BI file with interactive dashboard (KPIs, charts, tables, maps, slicers).
-   **`lambda_function.py`** – AWS Lambda for automated ETL on S3 events.
-   **`pyspark_init_etl.py`** – Initial ETL of raw YouTube data using PySpark.
-   **`pyspark_join_code.py`** – Joins datasets and performs transformations using PySpark.

---

## AWS Services in Action

Below are snapshots showing the working AWS services used in this project.

<table>
  <tr>
    <td><img src="static/image1.png" alt="AWS Screenshot 1" width="300"/></td>
    <td><img src="static/image2.png" alt="AWS Screenshot 2" width="300"/></td>
    <td><img src="static/image3.png" alt="AWS Screenshot 3" width="300"/></td>
  </tr>
  <tr>
    <td><img src="static/image4.png" alt="AWS Screenshot 4" width="300"/></td>
    <td><img src="static/image5.png" alt="AWS Screenshot 5" width="300"/></td>
    <td><img src="static/image6.png" alt="AWS Screenshot 6" width="300"/></td>
  </tr>
</table>

---

## Let's Connect

[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/923074315952)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:asadali27232@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/asadali27232/)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/asadalighaffar)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/asadali27232)
[![Personal Website](https://img.shields.io/badge/Personal%20Website-24292e?style=for-the-badge&logo=react&logoColor=white&color=purplr)](https://asadali27232.github.io/asadali27232)
