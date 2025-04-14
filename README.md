# Nutrition & Wellness Data Pipeline

This project is a **data pipeline** designed to streamline the ingestion of structured wellness data from an Excel file and insert it into a database, where further analysis and machine learning can be performed.

---

## Project Overview

- **Source**: Excel file located in the `Files` directory
- **Target**: SQLite database
- **Input Sheets**: `food`, `diet`, `workouts`, `mood`, and `logs`
- **Workflow**:
  1. Read structured data from Excel
  2. Parse and clean input data
  3. Insert valid entries into the database
  4. Remove processed entries from the Excel file

---

## Objective

Once enough data has been collected, the pipeline will enable the use of machine learning models to discover correlations between:

- **Mood** ↔ **Activity**
- **Mood** ↔ **Diet**
- **Diet** ↔ **Activity**
- And the full loop: **Mood ↔ Diet ↔ Activity ↔ Mood**

---

##  Future Plans

- Feature engineering for time-based and contextual insights (e.g. time of day, day of week)
- Model development using classification, regression, and clustering algorithms
- Visualizations to understand trends and predictions

---

## Technologies Used

- **Python 3.11**
- **Pandas** for Excel parsing
- **SQLAlchemy** for ORM and database operations
- **SQLite** as a local database
- **Future stack: scikit-learn, XGBoost, TensorFlow, etc.**

---

## Notes

- This project is currently in a data collection and ingestion phase.
- Database entries are structured for clean modeling downstream.
- The Excel file acts as a temporary staging environment for daily inputs.

---

## Machine Learning Goals

With enough samples, potential ML targets include:

- Predicting mood from diet and exercise
- Forecasting cravings or weight trends
- Clustering days by similarity in habits and emotional states
- Clustering workouts by weights and effects on mood

---

## Folder Structure

```text
nutrition_workouts/
├── Files/
│   └── nutrition_workouts.xlsx
├── nutrition.db
├── insert.py
├── queries.py
├── main.py
└── README.md