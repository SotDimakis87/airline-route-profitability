# ✈️ Airline Route Profitability — Data Engineering ETL Pipeline

## 📌 Project Overview

This project is an end-to-end **Data Engineering ETL pipeline** built to process airline operational data and load it into a structured data warehouse for downstream analytics.

The dataset contains more than **7,500 flight records** across international routes, including short-haul, medium-haul, and long-haul operations across multiple aircraft types.

The pipeline is designed to simulate a real-world airline data platform, transforming raw operational data into a **clean, validated, and analytics-ready fact table**.

The dataset reflects operations connected to **Dubai International Airport (DXB)**, a major global aviation hub.

---



## 📊 Dataset

This project uses a dataset from Kaggle licensed under **CC BY 4.0**.

Source:  
https://www.kaggle.com/datasets/waleedfaheem/airline-route-profitability-and-cost-analysis/data

The dataset contains simulated flight-level operational and financial data for airline route profitability analysis.

### Raw Data Includes:
- Flight-level operational records
- Route information (Origin → Destination)
- Aircraft types and capacity
- Passenger counts
- Revenue breakdown (ticket + ancillary)
- Cost breakdown (fuel, crew, maintenance, etc.)
- Profitability fields

---

## 🏗️ ETL Pipeline Architecture

```
RAW CSV DATA
│
▼
EXTRACT (extract.py)
│
▼
TRANSFORM (transform.py)
│
├── Data profiling
├── Missing value handling
├── Data validation rules
├── Route standardization checks
├── Geospatial distance computation
└── KPI generation (RPK, ASK, RASK, CASK, Yield)
│
▼
LOAD (load_to_postgres.py)
│
▼
POSTGRESQL DATA WAREHOUSE
│
▼
FACT TABLE: fact_airline_flights
```

---

## ⚙️ Transformation Layer

The transformation stage ensures data quality and prepares the dataset for analytical consumption.

### Data Quality Controls
- Duplicate detection
- Missing value handling for operational cost fields
- Route consistency validation (Origin → Destination format)
- Capacity constraint validation (Passengers ≤ Aircraft Capacity)

### Feature Engineering
- Flight distance calculation using geodesic coordinates
- Derived per-unit metrics:
  - Revenue per passenger
  - Cost per passenger
  - Profit per passenger

### Aviation KPI Generation
- **RPK** — Revenue Passenger Kilometers  
- **ASK** — Available Seat Kilometers  
- **RASK** — Revenue per Available Seat Kilometer  
- **CASK** — Cost per Available Seat Kilometer  
- **Yield** — Revenue per Revenue Passenger Kilometer  

---

## 🧱 Data Warehouse Model

The final output of the ETL pipeline is a **single fact table** stored in PostgreSQL: **fact_airline_flights**

This table contains:
- Cleaned flight operational data
- Standardized route information
- Financial metrics (revenue, cost, profit)
- Engineered aviation KPIs (RPK, ASK, RASK, CASK, Yield)

It serves as the analytical layer for downstream consumption.

---

## 🛠️ Tech Stack

- Python (ETL processing)
- Pandas (data transformation)
- SQLAlchemy (database connectivity)
- PostgreSQL (data warehouse)
- Geopy (distance calculation)
---


## 👤 Author

**Built by:** Sotiris Dimakis  
Project developed as part of Data Engineering Bootcamp at Big Blue Data Academy 
