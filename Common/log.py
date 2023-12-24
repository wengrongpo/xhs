import os
import sys
from loguru import logger


def log():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    log_file_path = os.path.join(base_dir, 'Log/LOG.log')
    err_log_file_path = os.path.join(base_dir, 'Log/error.log')
    logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
    logger.add(log_file_path, rotation="500 MB", encoding='utf-8')  # Automatically rotate too big file
    logger.add(err_log_file_path, rotation="500 MB", encoding='utf-8',
               level='ERROR')
    return logger  # Automatically rotate too big file


log()
