from lesson5.models import XRate, peewee_datetime
from lesson5.config import logging, LOGGER_CONFIG

log = logging.getLogger("TestApi")
fh = logging.FileHandler(LOGGER_CONFIG["file"])
fh.setFormatter(LOGGER_CONFIG["formatter"]) 
fh.setLevel(LOGGER_CONFIG["level"])
log.addHandler(fh)
log.setLevel(LOGGER_CONFIG["level"])

def update_xrates(from_currency, to_currency):
    log.info("Started update for: %s=>%s" % (from_currency, to_currency))
    xrate = XRate.select().where(XRate.from_currency == from_currency,
                                 XRate.to_currency == to_currency).first()

    log.debug("rate before: %s", xrate)
    xrate.rate += 0.01
    xrate.updated = peewee_datetime.datetime.now()
    xrate.save()

    log.debug("rate after: %s", xrate)
    log.info("Finished update for: %s=>%s" % (from_currency, to_currency))
