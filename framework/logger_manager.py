import logging
from pathlib import Path

from utilities.datetime_utils import DateTimeUtils
from logging.handlers import RotatingFileHandler

class LoggerManager:

    @staticmethod
    def get_logger(name: str):

        logger = logging.getLogger(name)

        if logger.handlers:
            return logger

        logger.setLevel(logging.INFO)

        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)

        file_handler = RotatingFileHandler(
            log_dir / f"{DateTimeUtils.timestamp()}.log",
            maxBytes=5_000_000,
            backupCount=5,
            encoding="utf-8"
        )

        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger