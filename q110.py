# Log debug, info, warning, and error messages to a file.
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)
logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")