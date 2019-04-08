import logging

DB_NAME = "licenses.db"
LOGGER_CONFIG = dict(level=logging.INFO, file="app.log", formatter=logging.Formatter("%(asctime)s [%(levelname)s] - %(name)s:%(message)s"))

log = logging.getLogger("LicenseApp")
fh = logging.FileHandler(LOGGER_CONFIG["file"])
fh.setLevel(LOGGER_CONFIG["level"])
fh.setFormatter(LOGGER_CONFIG["formatter"])
log.addHandler(fh)
log.setLevel(LOGGER_CONFIG["level"])