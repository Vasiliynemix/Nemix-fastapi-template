import logging
from pathlib import Path

from app.config import conf

BASE_DIR = Path(__file__).parent.parent


class MyAppLogger:
    def __init__(self):
        self.logger = logging.getLogger("my_app")
        self.logger.setLevel(logging.DEBUG)

        path_to_log_file = f"{BASE_DIR}/{conf.logger.file_name}"
        file_handler = logging.FileHandler(path_to_log_file)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def log(self, message, level=logging.INFO):
        if level == logging.DEBUG:
            self.logger.debug(message)
        elif level == logging.INFO:
            self.logger.info(message)
        elif level == logging.WARNING:
            self.logger.warning(message)
        elif level == logging.ERROR:
            self.logger.error(message)
        elif level == logging.CRITICAL:
            self.logger.critical(message)


logger = MyAppLogger()
