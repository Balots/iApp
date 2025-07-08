import logging
import sys


console_handler = logging.StreamHandler(sys.stdout)
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[console_handler]
)