import sys
import logging
from datetime import datetime

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler("backup.log", "a")
logger.addHandler(handler)


def log_info(message):
    log(message, "info")

def log_error(message):
    log(message, "error")
    
def log_warning(message):
    log(message, "warning")

def log(message, type):
    now = datetime.now()    
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    if type == "info":
        logger.info(f"{timestamp} - {message}")
    if type == "error":
        logger.error(f"{timestamp} - {message}")
    if type == "warning":
        logger.warning(f"{timestamp} - {message}")


def main() -> int:
    log()
    return 0


if __name__ == "__main__":
    sys.exit(main())
