# Retail Data Cost Analysis

This repository showcases a retail cost analysis workflow using the UCI Online Retail dataset. It combines a Python data processing script with an embedded Tableau dashboard to provide insights into product and vendor cost metrics.

## Project Structure

* **process\_retail\_data.py**
  A Python script that:

  1. Loads and cleans the raw `Online_Retail.xlsx` dataset.
  2. Standardizes records and handles missing or inconsistent entries.
  3. Calculates key cost metrics (e.g., modeled “should‑cost” vs. vendor quotes).
  4. Outputs the transformed data as `Processed_Retail_Data.csv`.

* **Online\_Retail.xlsx**
  The original UCI Online Retail transactions dataset, containing order-level details for product purchases.

* **Processed\_Retail\_Data.csv**
  The cleaned and enriched CSV featuring aggregated cost calculations and data quality checks.

## Tableau Dashboard

![Dashboard Preview](tableau_dashboard/preview.png)

What it shows:

* **Cost Trends Over Time:** A line chart showing average modeled should-cost and average vendor quotes by date, highlighting price fluctuations and seasonal trends.
* **Price Distribution:** A histogram and box plot of item prices and quantities to identify common price points, detect outliers, and understand overall variation.
* **Should‑Cost vs. Vendor Quotes:** A scatter plot comparing modeled should-cost against actual vendor quotes, revealing discrepancies and potential cost‑saving opportunities.

 * `MyTableauDashboard.twbx` – packaged Tableau workbook

View the fully interactive dashboard here:
https://emma-lewis.github.io/Retail_Data/

## Summary

A reproducible workflow that:

1. **Cleans and transforms** raw retail transaction data using Python.
2. **Calculates actionable cost insights**, comparing vendor quotes against modeled should‑costs.
3. **Visualizes** results in an interactive Tableau dashboard embedded above.

## Data Citation

Chen, D. (2015). *Online Retail* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33.
