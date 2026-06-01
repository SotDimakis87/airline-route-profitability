# Data Cleaning & Transformation Rules

This document describes all data quality checks and transformations applied in the ETL pipeline for the Airline Route Profitability dataset.

---

## 1. Data Quality Checks

- Checked dataset for duplicate records (no duplicates found)
- Assessed missing values across all columns
- Verified integrity of critical business columns:
  - Route
  - Aircraft Type
  - Total Revenue
  - Total Cost
  - Profit

---

## 2. Missing Value Handling

The following imputations were applied:

- Filled missing values in `Ancillary_Revenue` with 0
- Filled missing values in `Catering_Cost` with 0
- Filled missing values in `Handling_Cost` with 0

---

## 3. Data Validation Rules

- Route consistency check:
  - Validated that `Route = Origin + "-" + Destination`

- Capacity constraint validation:
  - Ensured `Passengers <= Aircraft_Capacity`

---

## 4. Feature Engineering

### Distance Calculation
- Computed `Distance_KM` using geodesic distance between airports

---

### Unit Economics Metrics
- Revenue per Passenger = Total_Revenue / Passengers
- Cost per Passenger = Total_Cost / Passengers
- Profit per Passenger = Profit / Passengers

---

### Aviation KPIs

- RPK (Revenue Passenger Kilometers) = Passengers × Distance_KM
- ASK (Available Seat Kilometers) = Aircraft_Capacity × Distance_KM
- RASK = Total_Revenue / ASK
- CASK = Total_Cost / ASK
- Yield = Total_Revenue / RPK

---

## 5. Output Standardization

- Standardized all column names to lowercase before loading into PostgreSQL