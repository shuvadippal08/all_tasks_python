import logging
import os
from config import LOG_DIR, LOG_FILE

os.makedirs(LOG_DIR,exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR,LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | Line:%(lineno)d | %(message)s",
    # force=True,
)

logger = logging.getLogger(__name__)