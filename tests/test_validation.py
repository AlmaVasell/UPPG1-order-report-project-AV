import pandas as pd
import pytest

from src.order_report.validation import validate_orders


def test_missing_required_column_raises_error():
    """Kontrollerar att saknade obligatoriska kolumner ger fel."""
    data = pd.DataFrame(
        {
            "order_id": [1],
            "order_date": ["2026-01-01"],
            "customer_id": [100],
            "region": ["North"],
            "product_category": ["Electronics"],
            "quantity": [2],
            "unit_price": [100.0],
            "discount": [0.1],
            # returned saknas medvetet
        }
    )

    with pytest.raises(ValueError, match="returned"):
        validate_orders(data)

def test_empty_data_raises_error():
    """Kontrollerar att tom orderdata ger ett tydligt fel."""
    data = pd.DataFrame()

    with pytest.raises(ValueError, match="Orderdatan är tom"):
        validate_orders(data)