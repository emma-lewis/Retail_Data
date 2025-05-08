"""
process_retail_data.py

A script to process the UCI Online Retail dataset by:
  1. Loading and cleaning raw sales data.
  2. Aggregating sales by SKU.
  3. Simulating cost components (material, labor, packaging, overhead %).
  4. Computing overhead cost as a separate column.
  5. Calculating should-cost as the sum of all cost components.
  6. Generating two vendor quotes (one below, one above cost) and computing variances.
  7. Exporting the enriched dataset to CSV.
"""

import logging
from pathlib import Path

import numpy as np
import pandas as pd

# Configuration
INPUT_FILE = Path('Online_Retail.xlsx')
OUTPUT_FILE = Path('Processed_Retail_Data.csv')


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def load_data(filepath: Path) -> pd.DataFrame:
    """Load the raw retail data from an Excel file."""
    return pd.read_excel(filepath)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the dataset by:
      - Dropping rows missing CustomerID.
      - Filtering out non-positive quantities.
    """
    df = df.dropna(subset=['CustomerID'])
    return df[df['Quantity'] > 0].copy()


def aggregate_sales(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate total units sold and total sales by product.
    """
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    return (
        df.groupby(['StockCode', 'Description'])
          .agg(TotalUnitsSold=('Quantity', 'sum'),
               TotalSales=('TotalPrice', 'sum'))
          .reset_index()
    )


def simulate_cost_components(df: pd.DataFrame, seed: int = 42) -> pd.DataFrame:
    """
    Simulate cost components and compute overhead cost & should-cost.

    - MaterialCost: $1.50–$5.00
    - LaborCost: $1.00–$3.00
    - PackagingCost: $0.20–$1.00
    - OverheadPct: 10%–25%
    - OverheadCost = (Material + Labor + Packaging) * OverheadPct
    - ShouldCost = Material + Labor + Packaging + OverheadCost
    """
    np.random.seed(seed)
    n = len(df)

    # Base cost components
    df['MaterialCost']  = np.random.uniform(1.5, 5.0, n)
    df['LaborCost']     = np.random.uniform(1.0, 3.0, n)
    df['PackagingCost'] = np.random.uniform(0.2, 1.0, n)
    df['OverheadPct']   = np.random.uniform(0.10, 0.25, n)

    # Explicit overhead in dollars
    df['OverheadCost'] = (
        df['MaterialCost']
      + df['LaborCost']
      + df['PackagingCost']
    ) * df['OverheadPct']

    # ShouldCost = sum of all components
    df['ShouldCost'] = (
        df['MaterialCost']
      + df['LaborCost']
      + df['PackagingCost']
      + df['OverheadCost']
    )
    return df


def calculate_quotes_and_discrepancies(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate two vendor quotes and compute:
      - CostDiscrepancy = VendorQuote – ShouldCost
      - DiscrepancyPct (%) = CostDiscrepancy / ShouldCost * 100
      - TotalDiscrepancyImpact = CostDiscrepancy * TotalUnitsSold
      - TotalVendorCost = VendorQuote * TotalUnitsSold
    """
    n = len(df)

    # Vendor1 always under-cost (negative discrepancy)
    df['Vendor1Quote'] = df['ShouldCost'] * np.random.uniform(0.90, 0.98, n)

    # Vendor2 always over-cost (positive discrepancy)
    df['Vendor2Quote'] = df['ShouldCost'] * np.random.uniform(1.02, 1.10, n)

    for vendor in ('Vendor1', 'Vendor2'):
        quote_col     = f'{vendor}Quote'
        diff_col      = f'CostDiscrepancy_{vendor}'
        pct_col       = f'DiscrepancyPct_{vendor}'
        impact_col    = f'TotalDiscrepancyImpact_{vendor}'
        total_cost_col= f'Total{vendor}Cost'

        df[diff_col]   = df[quote_col] - df['ShouldCost']
        df[pct_col]    = df[diff_col] / df['ShouldCost'] * 100
        df[impact_col] = df['TotalUnitsSold'] * df[diff_col]
        df[total_cost_col] = df['TotalUnitsSold'] * df[quote_col]

    return df


def save_data(df: pd.DataFrame, filepath: Path) -> None:
    """Save the final DataFrame to CSV."""
    df.to_csv(filepath, index=False)


def main():
    setup_logging()
    logging.info('Loading raw data...')
    raw_df = load_data(INPUT_FILE)

    logging.info('Cleaning data...')
    clean_df = clean_data(raw_df)

    logging.info('Aggregating sales...')
    agg_df = aggregate_sales(clean_df)

    logging.info('Simulating cost components and overhead...')
    cost_df = simulate_cost_components(agg_df)

    logging.info('Calculating quotes and discrepancies...')
    final_df = calculate_quotes_and_discrepancies(cost_df)

    logging.info(f'Saving enriched data to {OUTPUT_FILE}')
    save_data(final_df, OUTPUT_FILE)

    logging.info('Processing complete.')


if __name__ == '__main__':
    main()