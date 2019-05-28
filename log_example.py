import logging

log = logging.getLogger("LoggerName")
fh = logging.FileHandler("app.log")
fh.setLevel(logging.DEBUG)
fh.setFormatter(logging.Formatter(
    "%(asctime)s [%(levelname)s] - %(name)s:%(message)s"))
log.addHandler(fh)
log.setLevel(logging.DEBUG)

log.debug("Hello from app!")

