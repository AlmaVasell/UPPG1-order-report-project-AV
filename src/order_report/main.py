import logging
from pathlib import Path

from .config import ReportConfig
from .loading import load_orders
from .processing import clean_order_data, calculate_order_values
from .reporting import (
    create_overview,
    create_returns_by_category,
    create_sales_summary,
    save_report,
)
from .validation import validate_orders


def configure_logging() -> None:
    """Konfigurerar programmets logging."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
    )


def main() -> None:
    """Startar orderrapporten."""
    configure_logging()

    logger = logging.getLogger(__name__)
    logger.info("Startar orderrapport")

    config = ReportConfig(
        input_path=Path("data/orders.csv"),
        output_dir=Path("output"),
    )

    try:
        data = load_orders(config.input_path)

        validate_orders(data)

        data = clean_order_data(data)

        data = calculate_order_values(data)

        overview = create_overview(data)

        sales_by_category = create_sales_summary(
            data,
            "product_category",
        )

        sales_by_region = create_sales_summary(
            data,
            "region",
        )

        returns_by_category = create_returns_by_category(data)

        save_report(
            overview,
            config.output_dir,
            "overview.csv",
        )

        save_report(
            sales_by_category,
            config.output_dir,
            "sales_by_category.csv",
        )

        save_report(
            sales_by_region,
            config.output_dir,
            "sales_by_region.csv",
        )

        save_report(
            returns_by_category,
            config.output_dir,
            "returns_by_category.csv",
        )

        logger.info("Klart")

    except FileNotFoundError as error:
        logger.error(
            "Kunde inte läsa orderfilen: %s",
            error,
        )

    except ValueError as error:
        logger.error(
            "Ogiltig orderdata: %s",
            error,
        )


if __name__ == "__main__":
    main()