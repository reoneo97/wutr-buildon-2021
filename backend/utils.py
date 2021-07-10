from datetime import datetime
from loguru import logger

def get_current_timestamp()-> str:
    return datetime.now().isoformat()

def get_unix_timestamp() -> int:
    return int(datetime.now().timestamp())