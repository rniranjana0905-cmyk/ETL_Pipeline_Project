# 📊 Superstore Sales & Profit Analysis

## 🔍 Project Overview

This project analyzes sales and profit performance using a Superstore dataset. The goal is to identify trends, evaluate profitability, and provide business insights.

---

## 🎯 Objectives

* Analyze monthly sales and profit trends
* Identify top-performing categories and regions
* Evaluate profit margins and discount impact

---

## 🛠️ Tools Used

* Python (Pandas) – Data Cleaning
* SQL – Data Analysis
* Power BI – Dashboard Visualization

---

## 📂 Dataset

The dataset includes:

* Order Date, Ship Date
* Sales, Profit, Discount
* Category, Region, Segment

---

## ⚙️ Data Cleaning

* Converted date columns into proper datetime format
* Removed null and invalid values
* Handled missing data

---

## 📊 Key Analysis (SQL)

```sql
SELECT 
    DATE_FORMAT(`Order Date`, '%Y-%m') AS Month,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    ROUND(SUM(Profit)/SUM(Sales)*100,2) AS Profit_Margin
FROM superstore
GROUP BY Month
ORDER BY Month;
```

---

## 📈 Dashboard

The dashboard includes:

* Monthly Sales & Profit Trends
* Category-wise performance
* Regional analysis
* KPI metrics (Sales, Profit, Margin)

---

## 💡 Key Insights

* Sales show an increasing trend over time
* Profit margins fluctuate due to discounting
* Technology category generates the highest profit
* Certain regions outperform others consistently

---

## 📸 Dashboard Preview

(Add your screenshot here)

---

## 🚀 Conclusion

This analysis helps understand sales performance and highlights opportunities to improve profitability.

---

