# Data Dictionary — Airline Route Profitability Dataset

This document describes each column in the `fact_airline_flights` table used in the ETL pipeline.

---

## Flight Information

| Column | Description |
|--------|-------------|
| flight_number | Unique identifier for each flight |
| flight_date | Date of the flight operation |
| origin | Departure airport IATA code |
| destination | Arrival airport IATA code |
| route | Combined route in format ORIGIN-DESTINATION |
| distance_km | Great-circle distance between origin and destination in kilometers |

---

## Aircraft Information

| Column | Description |
|--------|-------------|
| aircraft_type | Type/model of aircraft used for the flight |
| aircraft_capacity | Maximum number of available seats on the aircraft |

---

## Demand & Operations

| Column | Description |
|--------|-------------|
| passengers | Number of passengers carried on the flight |
| load_factor | Percentage of occupied seats (passengers / capacity) |
| flight_hours | Duration of the flight in hours |
| season | Season in which the flight occurred (e.g., Summer, Winter) |
| route_category | Classification of route (e.g., Short/Medium/Long haul) |
| demand_level | Demand intensity category (e.g., Low, Medium, High) |

---

## Revenue Components

| Column | Description |
|--------|-------------|
| ticket_revenue | Revenue generated from ticket sales |
| ancillary_revenue | Revenue from additional services (baggage, upgrades, etc.) |
| total_revenue | Total revenue (ticket + ancillary) |

---

## Cost Components

| Column | Description |
|--------|-------------|
| fuel_cost | Fuel expenses for the flight |
| maintenance_cost | Aircraft maintenance costs |
| crew_cost | Pilot and cabin crew costs |
| depreciation_cost | Aircraft depreciation allocation |
| insurance_cost | Insurance costs per flight |
| airport_fees | Charges paid to airports |
| catering_cost | In-flight catering expenses |
| handling_cost | Ground handling costs |
| navigation_fees | Air traffic and navigation charges |
| sales_distribution_cost | Ticket distribution and commission costs |
| passenger_service_cost | Passenger-related service expenses |
| overhead_cost | General operational overhead allocation |
| marketing_cost | Marketing and promotional expenses |
| it_systems_cost | IT infrastructure and systems costs |
| total_cost | Total operational cost of the flight |

---

## Profitability Metrics

| Column | Description |
|--------|-------------|
| profit | Net profit (total_revenue - total_cost) |
| profit_margin | Profit as a percentage of revenue |

---

## Unit Economics (Per Passenger)

| Column | Description |
|--------|-------------|
| revenue_per_passenger | Average revenue generated per passenger |
| cost_per_passenger | Average cost per passenger |
| profit_per_passenger | Average profit per passenger |

---

## Aviation KPIs

| Column | Description |
|--------|-------------|
| rpk | Revenue Passenger Kilometers (passengers × distance_km) |
| ask | Available Seat Kilometers (capacity × distance_km) |
| rask | Revenue per Available Seat Kilometer (total_revenue / ASK) |
| cask | Cost per Available Seat Kilometer (total_cost / ASK) |
| yield | Revenue per Revenue Passenger Kilometer (total_revenue / RPK) |
