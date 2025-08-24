# utils/logging_config.py

import logging
import time
from pathlib import Path

def setup_logging(log_dir: str):
    """
    Configures a logger to output to both console and a time-stamped file.
    
    This function ensures that any existing logging handlers are removed
    before adding new ones, preventing duplicate log messages in
    interactive environments like Jupyter.
    """
    log_dir_path = Path(log_dir)
    log_dir_path.mkdir(parents=True, exist_ok=True)
    
    # Create a unique filename for each run
    log_filename = time.strftime("benchmark_run_%Y-%m-%d_%H-%M-%S.log")
    log_filepath = log_dir_path / log_filename

    # Get the root logger and remove existing handlers
    logger = logging.getLogger()
    if logger.hasHandlers():
        logger.handlers.clear()

    # Configure the logger
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(log_filepath),
            logging.StreamHandler()
        ]
    )
    logging.info(f"Logging configured. Log file at: {log_filepath}")