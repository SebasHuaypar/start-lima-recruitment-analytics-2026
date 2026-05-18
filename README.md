# START Lima Analytics Dashboard

An end-to-end analytics engineering project built to process, clean, normalize, and analyze applicant data from the START Lima recruitment platform.

This project extracts application data from Supabase, transforms semi-structured JSON responses into analytics-ready tables using Python and Pandas, and loads the cleaned data back into Supabase for business intelligence and dashboarding purposes.

---

# Project Overview

The recruitment platform stores applicant responses inside a JSON field (`answers`) within the `applications` table.

This pipeline:

- Extracts applications from Supabase
- Parses and flattens JSON responses
- Cleans and standardizes raw data, ignoring irrelevant fields
- Generates engagement scores, text length metrics, and date features
- Normalizes university names, acquisition channels, and education types
- Loads analytics-ready data into a clean table (`applications_clean`)
- Prepares the dataset for Power BI dashboards and future analytics workflows

---

# Tech Stack

- Python
- Pandas
- Supabase
- PostgreSQL
- dotenv
- Power BI

---

# ETL Pipeline Architecture

```text
applications (raw data)
        |
    Extract
        |
 JSON Parsing & Flattening
        |
 Feature Engineering & Normalization
        |
applications_clean (analytics-ready)
        |
     Power BI
```

---

# Project Structure

```text
start-lima-analytics/
|
|-- pipeline/
|   |-- config.py
|   |-- extract.py
|   |-- transform.py
|   |-- normalize_data.py
|   |-- normalize/
|   |   |-- __init__.py
|   |   |-- channels.py
|   |   |-- helpers.py
|   |   |-- universities.py
|   |-- load.py
|   |-- pipeline.py
|
|-- .env
|-- requirements.txt
|-- README.md
```

---

# Features Implemented

## Data Extraction

- Connection to Supabase PostgreSQL database
- Extraction of raw application records

## Data Transformation

- JSON parsing from application responses
- Flattening nested applicant data into tabular format
- Extraction of datetime components (Year, Month, Week, Day)

## Feature Engineering

- Calculation of text lengths for open-ended questions (goals, projects, activities)
- Creation of boolean flags (has_linkedin, is_submitted)
- Implementation of a custom Engagement Score system (0-4) based on applicant effort
- Classification of engagement tiers (Low, Medium, High)

## Data Normalization

- Regular expression cleaning for prefixes and tricky text patterns
- Robust dictionary-mapping for University variants to canonical names and BI-friendly abbreviations
- Smart inference and mapping for acquisition channels (WhatsApp, LinkedIn, Email, Referral)
- Categorization of education types (University, Institute, Self-Taught)

## Data Loading

- Safe null and datetime handling for JSON serialization compatibility
- Upsert logic based on primary keys to avoid duplicates
- Automated synchronization with Supabase

---

# Example Normalization

| Raw Value | Canonical Name | Short Version |
| --------- | ----------------------------------------- | ------------- |
| upc | Universidad Peruana de Ciencias Aplicadas | UPC |
| dnt upao | Universidad Privada Antenor Orrego | UPAO |
| wsp | WhatsApp | WhatsApp |
| wssp | WhatsApp | WhatsApp |

---

# Current Status

- [x] Modular ETL pipeline completed
- [x] Data normalization layer completed
- [x] Analytics-ready database table completed
- [x] Power BI dashboard integration
- [x] KPI tracking and recruitment analytics
- [ ] Portfolio web integration

---

# Future Improvements

## Data Engineering
- Incremental data loading (avoiding full table scans during upsert)
- Automated scheduled runs via CI/CD or cron jobs

## Power BI Dashboard
- **Executive Storytelling:** Refining the narrative flow and actionable insights for stakeholders
- **UX & Layout:** Implementing intuitive navigation and a cleaner visual hierarchy
- **START Lima Branding:** Applying corporate design tokens (colors, custom typography)
- **Advanced DAX:** Implementing time-intelligence metrics (e.g., Week-over-Week growth)

---

# Author

<div align="center">

## Sebastián Huaypar Acurio

Computer Science Student @ UNI  
AI, Data Science & Analytics Engineering Enthusiast  
[LinkedIn](https://www.linkedin.com/in/sebashuaypar)

</div>
