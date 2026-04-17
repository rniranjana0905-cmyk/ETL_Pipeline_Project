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
![stucture](https://github.com/user-attachments/assets/e4332a7a-a8c4-4629-a466-3a7995932a65)

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python etl.py

📊 Output
Data is stored in PostgreSQL table: sales
![SQL Output 1](https://github.com/user-attachments/assets/fff89211-7cff-49a1-b30c-fe4655006246)

![SQL Output 2](https://github.com/user-attachments/assets/b7ea0e2d-b385-4fc3-bb7a-e601fef7a273)

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

