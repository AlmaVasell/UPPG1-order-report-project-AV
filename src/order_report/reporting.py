import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)


def create_overview(data: pd.DataFrame) -> pd.DataFrame:
    """Skapar en övergripande sammanfattning av orderdatan."""
    total_sales = round(
        data["discounted_value"].sum(),
        2,
    )

    number_of_orders = data["order_id"].nunique()
    number_of_returns = int(data["returned"].sum())

    return pd.DataFrame(
        {
            "metric": [
                "total_sales",
                "order_count",
                "return_count",
            ],
            "value": [
                total_sales,
                number_of_orders,
                number_of_returns,
            ],
        }
    )


def create_sales_summary(
    data: pd.DataFrame,
    group_by: str,
) -> pd.DataFrame:
    """Skapar en försäljningssammanfattning för vald kolumn."""
    summary = (
        data.groupby(group_by, as_index=False)
        .agg(
            order_count=("order_id", "nunique"),
            total_sales=("discounted_value", "sum"),
            returns=("returned", "sum"),
        )
    )

    summary["total_sales"] = summary["total_sales"].round(2)

    summary["return_rate"] = (
        summary["returns"] / summary["order_count"]
    ).round(3)

    return summary.sort_values(
        "total_sales",
        ascending=False,
    ).reset_index(drop=True)


def create_returns_by_category(
    data: pd.DataFrame,
) -> pd.DataFrame:
    """Skapar en sammanfattning av returer per produktkategori."""
    summary = (
        data.groupby("product_category", as_index=False)
        .agg(
            order_count=("order_id", "nunique"),
            returns=("returned", "sum"),
        )
    )

    summary["return_rate"] = (
        summary["returns"] / summary["order_count"]
    ).round(3)

    return summary.sort_values(
        "return_rate",
        ascending=False,
    ).reset_index(drop=True)


def save_report(
    report: pd.DataFrame,
    output_dir: Path,
    filename: str,
) -> None:
    """Sparar en rapport som CSV."""
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / filename
    report.to_csv(output_path, index=False)

    logger.info("Sparade %s", filename)