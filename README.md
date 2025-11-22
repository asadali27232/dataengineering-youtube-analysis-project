# Data Engineering YouTube Analysis Project

**Author:** Darshil Parmar  

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

| Service | Purpose |
|---------|---------|
| **Amazon S3** | Object storage service for scalable, secure, and available data storage. |
| **AWS IAM** | Manage access and permissions to AWS resources securely. |
| **AWS Glue** | Serverless data integration for discovery, transformation, and preparation. |
| **AWS Lambda** | Run code without managing servers, used for automation tasks. |
| **AWS Athena** | Interactive querying service for data stored in S3 using SQL. |

**Visualization:**  
- **Power BI**: Desktop/cloud tool used to create interactive dashboards, charts, tables, and slicers.  

---

## Dataset Used

- **Source:** [Kaggle - Trending YouTube Videos Dataset](https://www.kaggle.com/datasets/datasnaek/youtube-new)  
- **Description:**  
  The dataset contains statistics (CSV files) on daily trending YouTube videos across multiple regions.  
  Each file contains up to 200 trending videos per day and includes the following fields:  
  - `video_id`, `title`, `channel_title`, `publish_time`, `tags`, `views`, `likes`, `dislikes`, `description`, `comment_count`  
  - `category_id` linked via JSON files for each region  

- **Data Type:** Structured CSV files and JSON for category mapping.  

---

## Architecture Diagram

```text
            +-------------------+
            |   YouTube Data    |
            | (CSV + JSON Files)|
            +---------+---------+
                      |
                      v
             +------------------+
             |  AWS S3 (Raw)    |
             +---------+--------+
                       |
                       v
             +------------------+
             |   AWS Glue ETL   |
             | Transform & Clean|
             +---------+--------+
                       |
                       v
             +------------------+
             | AWS S3 (Processed)|
             +---------+--------+
                       |
                       v
          +-----------------------+
          | AWS Athena / Queries  |
          +---------+-------------+
                    |
                    v
            +----------------+
            |   Power BI     |
            |  Dashboard     |
            +----------------+
