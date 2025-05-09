#!/usr/bin/env python3
"""
calculate_margin_recovery.py

Module for computing total should-cost, quoted cost, potential savings,
and margin recovery percentage from a processed retail dataset CSV.
"""

import argparse
import pandas as pd


def compute_margin_recovery(
    df: pd.DataFrame,
    cost_components: list[str],
    quote_col: str,
    qty_col: str | None = None
) -> dict[str, float]:
    """
    Compute total should-cost, quoted cost, savings, and recovery percentage.

    Args:
        df (pd.DataFrame): DataFrame containing cost and quote data.
        cost_components (list[str]): List of column names for cost components.
        quote_col (str): Column name for vendor quoted price.
        qty_col (str, optional): Column name for quantity. If None or not present,
            assumes per-unit cost without quantity multiplication.

    Returns:
        dict[str, float]: A dictionary with keys:
            - 'total_should_cost'
            - 'total_quoted_cost'
            - 'total_savings'
            - 'recovery_pct'
    """
    df_work = df.copy()

    # Calculate per-unit should cost and quoted cost
    df_work["should_cost"] = df_work[cost_components].sum(axis=1)
    df_work["quoted_cost"] = df_work[quote_col]

    # Calculate total costs, considering quantity if provided
    if qty_col and qty_col in df_work.columns:
        df_work["total_should_cost"] = df_work["should_cost"] * df_work[qty_col]
        df_work["total_quoted_cost"] = df_work["quoted_cost"] * df_work[qty_col]
    else:
        df_work["total_should_cost"] = df_work["should_cost"]
        df_work["total_quoted_cost"] = df_work["quoted_cost"]

    # Aggregate totals
    total_should = df_work["total_should_cost"].sum()
    total_quoted = df_work["total_quoted_cost"].sum()
    total_savings = total_should - total_quoted
    recovery_pct = (total_savings / total_should) * 100 if total_should else 0.0

    return {
        "total_should_cost": total_should,
        "total_quoted_cost": total_quoted,
        "total_savings": total_savings,
        "recovery_pct": recovery_pct,
    }


def main() -> None:
    """
    Command-line interface to calculate margin recovery metrics
    from Processed_Retail_Data.csv using the correct column names.
    """
    parser = argparse.ArgumentParser(
        description="Calculate margin recovery from Processed_Retail_Data.csv."
    )
    parser.add_argument(
        "csv_path",
        help="Path to the processed retail data CSV file.",
    )
    parser.add_argument(
        "--cost-components",
        nargs="+",
        default=["MaterialCost", "LaborCost", "PackagingCost", "OverheadCost"],
        help="List of cost component column names (default matches your data).",
    )
    parser.add_argument(
        "--quote-col",
        default="Vendor1Quote",
        help="Column name for vendor quoted price (default: Vendor1Quote).",
    )
    parser.add_argument(
        "--qty-col",
        default="TotalUnitsSold",
        help="Column name for quantity (default: TotalUnitsSold).",
    )
    args = parser.parse_args()

    df = pd.read_csv(args.csv_path)
    metrics = compute_margin_recovery(
        df, args.cost_components, args.quote_col, args.qty_col
    )

    # Display the results
    print(f"Total should-cost:    ${metrics['total_should_cost']:.2f}")
    print(f"Total quoted cost:    ${metrics['total_quoted_cost']:.2f}")
    print(f"Potential savings:    ${metrics['total_savings']:.2f}")
    print(f"Margin recovery:      {metrics['recovery_pct']:.2f}%")
    

if __name__ == "__main__":
    main()