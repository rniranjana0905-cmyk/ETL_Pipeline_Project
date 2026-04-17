# ETL Sales Data Pipeline

## 🚀 Overview
This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using Python.

It extracts raw sales data from a CSV file, transforms it using pandas, and loads it into a PostgreSQL database hosted on Neon.

---

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
<img width="1919" height="934" alt="Screenshot 2026-04-16 195620" src="https://github.com/user-attachments/assets/a780a4ec-45b6-4ae2-9993-1a14b3c1cb44" />

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

## ❓ Problem Statement

Businesses often store sales data in raw formats (CSV), making it difficult to analyze.  
This pipeline automates cleaning and loading data into a database for analysis.
## 🎯 Impact

This pipeline enables structured storage of sales data, making it easier to run SQL queries and generate insights.
