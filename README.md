# Customer Data Pipeline

A Data Engineering project built with PySpark.

## Overview

This project simulates a complete data engineering pipeline:

CSV
→ Data Validation
→ Business Transformations
→ Parquet

## Dataset

Bank Customer Churn Prediction Dataset

## Technologies

- Python
- PySpark
- Pandas
- PostgreSQL
- Parquet

## Data Validation

The dataset was validated before any transformation.

### Row Count

Validated total number of records:

- Total Rows: 10,000

### Column Count

Validated dataset structure:

- Total Columns: 12

### Null Check

Validated missing values across all columns:

- No null values detected

### Duplicate Check

Validated duplicate records:

- No duplicate records detected

## Validation Evidence

images/validation_results.png

## Null Check Validation

images/null_check.png

## Business Transformations

### churn_desc

Business-friendly description of churn status:

| churn | churn_desc |
|--------|-------------|
| 0 | Active |
| 1 | Churned |

### age_group

Customer segmentation by age:

| Age | Group |
|-----|--------|
| < 30 | Young |
| 30 - 49 | Adult |
| >= 50 | Senior |

## Business Analysis

images/churn_by_age_group.png

## Output

Generated Parquet dataset:

```text
data/curated/customer_churn.parquet
```

## Project Structure

images/project_structure.png

## Repository Structure

```text
customer-data-pipeline
│
├── data
│   ├── raw
│   │   └── customer_churn.csv
│   │
│   └── curated
│       └── customer_churn.parquet
│
├── images
│   ├── validation_results.png
│   ├── null_check.png
│   ├── churn_by_age_group.png
│   └── project_structure.png
│
├── src
│   └── pipeline.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Key Outcomes

- Ingested CSV data using PySpark
- Performed data validation checks
- Verified null values and duplicate records
- Applied business transformations
- Generated Parquet output
- Simulated a real Data Engineering workflow