import logging

# Use Python’s logging module to log info and error messages in a script.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("This is an informational message.")
logging.error("This is an error message.")
