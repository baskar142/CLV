import logging
import os
from pathlib import Path
from datetime import datetime
from logging.handlers import RotatingFileHandler

# Project root (2 levels above this file)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
LOG_DIR = PROJECT_ROOT / "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_PATH = LOG_DIR / LOG_FILE

# Create logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Rotating File Handler
file_handler = RotatingFileHandler(
    filename=str(LOG_PATH),
    maxBytes=5*1024*1024,
    backupCount=5
)
file_handler.setFormatter(logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(console_handler)

# ✅ Confirmation message
print(f"✅ Logging to: {LOG_PATH}")
