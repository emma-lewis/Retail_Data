# Retail Data Cost Analysis Pipeline

This repository showcases a retail cost analysis pipeline built around the UCI Online Retail dataset. It combines Python data processing with interactive Tableau dashboards to provide end-to-end insights into product and vendor cost metrics.

## Project Structure

* **process\_retail\_data.py**
  A Python script that:

  1. Loads and cleans the raw `Online_Retail.xlsx` dataset.
  2. Standardizes records and handles missing or inconsistent entries.
  3. Calculates key cost metrics (e.g., calculated “should‑cost” vs. vendor quotes).
  4. Outputs the transformed data as `Processed_Retail_Data.csv`.

* **Online\_Retail.xlsx**
  The original UCI Online Retail transactions dataset, containing order-level details for product purchases.

* **Processed\_Retail\_Data.csv**
  The cleaned and enriched CSV featuring aggregated cost calculations and data quality flags.

* **tableau\_dashboard/**

  * `MyTableauDashboard.twbx` – a packaged Tableau workbook with interactive cost-analysis dashboards.
  * `preview.png` – a static snapshot of the primary dashboard view.

## Full Live Embed

View the fully interactive dashboard here:
https://emma-lewis.github.io/Retail_Data/

## Summary

A reproducible, version-controlled pipeline that:

1. **Cleans and transforms** raw retail transaction data using Python.
2. **Calculates actionable cost insights**, comparing vendor quotes against modeled should‑costs.
3. **Visualizes** results in an interactive Tableau dashboard embedded above.

This combination of data engineering, cost analysis, and dashboard development demonstrates core competencies for a Product Cost Associate and related analytical roles in retail and procurement.
