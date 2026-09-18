import pandas as pd
import pytest

from src.order_report.processing import (
    calculate_order_values,
    clean_order_data,
)
from src.order_report.reporting import (
    create_overview,
    create_returns_by_category,
    create_sales_summary,
)


def test_calculate_order_values():
    """Kontrollerar beräkning av ordervärde och rabatt."""
    data = pd.DataFrame(
        {
            "quantity": [2],
            "unit_price": [100.0],
            "discount": [0.10],
        }
    )

    result = calculate_order_values(data)

    assert result.loc[0, "order_value"] == pytest.approx(200.0)
    assert result.loc[0, "discounted_value"] == pytest.approx(180.0)

def test_create_overview():
    """Kontrollerar att overview-rapporten får rätt värden."""
    data = pd.DataFrame(
        {
            "order_id": [1, 2, 2],
            "discounted_value": [100.0, 200.0, 50.0],
            "returned": [False, True, False],
        }
    )

    result = create_overview(data)

    assert result.loc[0, "metric"] == "total_sales"
    assert result.loc[0, "value"] == pytest.approx(350.0)

    assert result.loc[1, "metric"] == "order_count"
    assert result.loc[1, "value"] == 2

    assert result.loc[2, "metric"] == "return_count"
    assert result.loc[2, "value"] == 1


def test_create_sales_summary_by_category():
    """Kontrollerar försäljningssammanfattning per kategori."""
    data = pd.DataFrame(
        {
            "order_id": [1, 2, 3],
            "product_category": [
                "Electronics",
                "Electronics",
                "Furniture",
            ],
            "discounted_value": [
                100.0,
                200.0,
                50.0,
            ],
            "returned": [
                False,
                True,
                False,
            ],
        }
    )

    result = create_sales_summary(
        data,
        "product_category",
    )

    electronics = result[
        result["product_category"] == "Electronics"
    ].iloc[0]

    assert electronics["order_count"] == 2
    assert electronics["total_sales"] == pytest.approx(300.0)
    assert electronics["returns"] == 1
    assert electronics["return_rate"] == pytest.approx(0.5)

def test_create_returns_by_category():
    """Kontrollerar returer per produktkategori."""
    data = pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4],
            "product_category": [
                "Electronics",
                "Electronics",
                "Furniture",
                "Furniture",
            ],
            "returned": [
                True,
                False,
                True,
                True,
            ],
        }
    )

    result = create_returns_by_category(data)

    electronics = result[
        result["product_category"] == "Electronics"
    ].iloc[0]

    furniture = result[
        result["product_category"] == "Furniture"
    ].iloc[0]

    assert electronics["order_count"] == 2
    assert electronics["returns"] == 1
    assert electronics["return_rate"] == pytest.approx(0.5)

    assert furniture["order_count"] == 2
    assert furniture["returns"] == 2
    assert furniture["return_rate"] == pytest.approx(1.0)

def test_clean_order_data():
    """Kontrollerar några viktiga delar av datarensningen."""
    data = pd.DataFrame(
        {
            "region": [None, " north "],
            "product_category": [" electronics ", None],
            "quantity": [None, "2"],
            "unit_price": [100.0, None],
            "discount": [None, "0.1"],
            "returned": ["yes", "false"],
        }
    )

    result = clean_order_data(data)

    assert result.loc[0, "region"] == "Unknown"
    assert result.loc[1, "region"] == "North"

    assert result.loc[0, "product_category"] == "Electronics"
    assert result.loc[1, "product_category"] == "Unknown"

    assert result.loc[0, "quantity"] == 1
    assert result.loc[1, "quantity"] == 2

    assert result.loc[1, "unit_price"] == pytest.approx(100.0)

    assert result.loc[0, "discount"] == pytest.approx(0.0)
    assert result.loc[1, "discount"] == pytest.approx(0.1)

    assert bool(result.loc[0, "returned"]) is True
    assert bool(result.loc[1, "returned"]) is False