import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)


def load_orders(file_path: Path) -> pd.DataFrame:
    """Läser orderdata från CSV."""
    if not file_path.exists():
        raise FileNotFoundError(f"Filen finns inte: {file_path}")

    logger.info("Läser orderdata från %s", file_path)

    data = pd.read_csv(file_path)

    logger.info("Läste %d rader", len(data))
    return data