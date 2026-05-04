# START Lima Analytics Dashboard

An end-to-end analytics engineering project built to process, clean, normalize, and analyze applicant data from the START Lima recruitment platform.

This project extracts application data from Supabase, transforms semi-structured JSON responses into analytics-ready tables using Python and Pandas, and loads the cleaned data back into Supabase for business intelligence and dashboarding purposes.

---

# Project Overview

The recruitment platform stores applicant responses inside a JSON field (`answers`) within the `applications_full` table.

This pipeline:

- Extracts submitted applications from Supabase
- Parses and flattens JSON responses
- Cleans and standardizes raw data
- Normalizes university names and categorical values
- Loads analytics-ready data into a clean table (`applications_clean`)
- Prepares the dataset for Power BI dashboards and future analytics workflows

---

# Tech Stack

- Python
- Pandas
- Supabase
- PostgreSQL
- dotenv
- Power BI (next stage)

---

# ETL Pipeline Architecture

```text
applications_full (raw data)
        ↓
    Extract
        ↓
 JSON Parsing & Flattening
        ↓
 Data Cleaning & Normalization
        ↓
applications_clean (analytics-ready)
        ↓
     Power BI
````

---

# Project Structure

```text
start-lima-analytics/
│
├── pipeline/
│   ├── config.py
│   ├── extract.py
│   ├── transform.py
│   ├── normalize.py
│   ├── load.py
│   └── pipeline.py
│
├── .env
├── requirements.txt
└── README.md
```

---

# Features Implemented

## Data Extraction

* Real-time connection to Supabase
* Extraction of submitted applications only

## Data Transformation

* JSON parsing from application responses
* Flattening nested applicant data into tabular format

## Data Cleaning

* Null and invalid value handling
* Removal of noisy text patterns
* Standardization of categorical values

## University Normalization

* Regex-based cleaning
* Semantic normalization using mapping dictionaries
* Consolidation of abbreviations and inconsistent naming

## Data Loading

* Upsert logic to avoid duplicates
* Automated synchronization with Supabase

---

# Example Normalization

| Raw Value | Normalized Value                          |
| --------- | ----------------------------------------- |
| UPC       | Universidad Peruana de Ciencias Aplicadas |
| PUCP      | Pontificia Universidad Católica del Perú  |
| UTP       | Universidad Tecnológica del Perú          |
| Usil      | Universidad San Ignacio de Loyola         |

---

# Current Status

- [x] Modular ETL pipeline completed
- [x] Data normalization layer completed
- [x] Analytics-ready database table completed
- [ ] Power BI dashboard integration
- [ ] KPI tracking and recruitment analytics
- [ ] Portfolio web integration

---

# Future Improvements

* Incremental processing
* Automated scheduled runs
* Additional categorical normalization
* Dimensional modeling
* Advanced recruitment KPIs
* Interactive dashboard embedding

---

# Author

<div align="center">

##  Sebastián Huaypar Acurio

Computer Science Student @ UNI  
AI, Data Science & Analytics Engineering Enthusiast  
[LinkedIn](https://www.linkedin.com/in/sebashuaypar)

</div>
