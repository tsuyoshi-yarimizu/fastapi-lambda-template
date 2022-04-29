import logging
import os
from logging import LogRecord, getLogger, StreamHandler, Formatter
from datetime import datetime
from pytz import timezone


class NoVendorClassFilter(logging.Filter):
    def filter(self, record: LogRecord) -> bool:
        module = record.pathname
        return 'src' in module


class CustomLogger:
    logger = None

    def __init__(self) -> None:
        self.logger = getLogger(__name__)
        log_level_name = os.environ.get('LOG_LEVEL', default='INFO')
        log_level = getattr(logging, log_level_name)
        self.logger.setLevel(log_level)

        if not self.logger.hasHandlers():
            handler = StreamHandler()
            handler.setLevel(log_level)

            def custom_time(*args):
                return datetime.now(timezone('Asia/Tokyo')).timetuple()

            formatter = Formatter(
                "[%(asctime)s][%(levelname)s][%(pathname)s:%(funcName)s:%(lineno)s] %(message)s\n",
                "%Y-%m-%d %H:%M:%S",
            )

            formatter.converter = custom_time
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

        self.logger.addFilter(NoVendorClassFilter())
        self.logger.propagate = False


custom_logger = CustomLogger().logger
