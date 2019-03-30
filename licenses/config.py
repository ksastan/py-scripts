import logging

DB_NAME = "licenses.db"
LOGGER_CONFIG = dict(level=logging.INFO, file="app.log", formatter=logging.Formatter("%(asctime)s [%(levelname)s] - %(name)s:%(message)s"))
