# ETL Sales Data Pipeline

## ❓ Problem Statement

Sales data is often stored in raw CSV formats, making it difficult to analyze and query efficiently.

This project builds an ETL pipeline to clean and load the data into a structured PostgreSQL database for better analysis.

## 🎯 Impact

This pipeline enables structured storage of sales data, making it easier to run SQL queries and generate insights.


## 🚀 Overview
This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using Python.

It extracts raw sales data from a CSV file, transforms it using pandas, and loads it into a PostgreSQL database hosted on Neon.

---
## 🏗️ Architecture

CSV File → Pandas (Transform) → PostgreSQL (Neon)

## 🛠️ Tech Stack
- Python
- pandas
- SQLAlchemy
- PostgreSQL (Neon)

---

## 🔄 ETL Pipeline

### 1. Extract
- Reads sales data from CSV file

### 2. Transform
- Cleans column names
- Handles missing values
- Converts date formats

### 3. Load
- Loads processed data into PostgreSQL database

---

## 📂 Project Structure
etl-sales-data-pipeline/
├── superstore_sales_sataset.csv
├── etl.py
├── db.py
├── requirements.txt
├── README.md
└── .gitignore


---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python etl.py

📊 Output
Data is stored in PostgreSQL table: sales

<img width="1911" height="827" alt="Screenshot 2026-04-16 195655" src="https://github.com/user-attachments/assets/1a1b7cf8-618b-4788-aeb7-259329005d92" />


🔐 Environment Variables

Create a .env file:

DB_URL=your_database_connection_string

💡 Features
End-to-end ETL pipeline
Data cleaning using pandas
Cloud database integration
Handles missing and invalid data


🚀 Future Improvements
Add Apache Airflow scheduling
Add dashboard (Power BI / Streamlit)
Add logging and monitoring
---

