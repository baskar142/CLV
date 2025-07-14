from CLV_Lux.logger import logging
logging.info("Logging setup complete.")

from CLV_Lux.exception import CLVException
import sys

try:
    # faulty logic
    1 / 0
except Exception as e:
    raise CLVException(e, sys)
