import logging

logger = logging.getLogger("temps")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("temps.log", encoding="utf-8")
file_handler.setLevel(logging.INFO)

logger.addHandler(file_handler)