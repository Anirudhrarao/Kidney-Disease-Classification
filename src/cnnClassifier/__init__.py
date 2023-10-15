import os
import sys
import logging
from pathlib import Path
from typing import List

def configure_logger(log_dir, log_filename):
    # Create the log directory if it doesn't exist
    os.makedirs(log_dir, exist_ok=True)

    # Configure the logger
    logger = logging.getLogger("cnnClassifierLogger")
    logger.setLevel(logging.INFO)

    # Create a formatter with the desired format
    formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s]: [%(filename)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # Create a file handler to log to a file
    log_filepath = os.path.join(log_dir, log_filename)
    file_handler = logging.FileHandler(log_filepath)
    file_handler.setFormatter(formatter)

    # Create a stream handler to log to the console
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger

# Example usage:
# logger = configure_logger("logs", "loggings.log")
# logger.info("This is a log message.")