import logging

import pandas as pd

logger = logging.getLogger(__name__)


def clean_order_data(data: pd.DataFrame) -> pd.DataFrame:
    """Rensar och konverterar orderdata till rätt datatyper."""
    result = data.copy()

    result["region"] = (
        result["region"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )

    result["product_category"] = (
        result["product_category"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )

    result["quantity"] = pd.to_numeric(
        result["quantity"], errors="coerce"
    ).fillna(1)

    result["unit_price"] = pd.to_numeric(
        result["unit_price"], errors="coerce"
    )

    result["unit_price"] = result["unit_price"].fillna(
        result["unit_price"].median()
    )

    result["discount"] = pd.to_numeric(
        result["discount"], errors="coerce"
    ).fillna(0)

    result["returned"] = (
        result["returned"]
        .fillna("false")
        .astype(str)
        .str.strip()
        .str.lower()
        .isin(["true", "yes", "1", "ja"])
    )

    logger.info("Orderdata rensad")
    return result


def calculate_order_values(data: pd.DataFrame) -> pd.DataFrame:
    """Beräknar ordervärde och värde efter rabatt."""
    result = data.copy()

    result["order_value"] = (
        result["quantity"] * result["unit_price"]
    )

    result["discounted_value"] = (
        result["order_value"] * (1 - result["discount"])
    )

    logger.info("Ordervärden beräknade")
    return result