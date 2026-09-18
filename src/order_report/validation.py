import logging

import pandas as pd

logger = logging.getLogger(__name__)


REQUIRED_COLUMNS = {
    "order_id",
    "order_date",
    "customer_id",
    "region",
    "product_category",
    "quantity",
    "unit_price",
    "discount",
    "returned",
}


def validate_orders(data: pd.DataFrame) -> None:
    """Validerar att orderdatan innehåller nödvändig information."""

    if data.empty:
        raise ValueError("Orderdatan är tom.")

    missing_columns = REQUIRED_COLUMNS - set(data.columns)

    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(
            f"Obligatoriska kolumner saknas: {missing}"
        )

    logger.info("Validering genomförd")