from texable.logger_config import setup_logging

setup_logging()

from texable.table import Table
from texable.custom_types import Alignment

__all__ = ["Table", "Alignment"]
