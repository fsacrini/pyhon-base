#!/usr/bin/env python3

import os
import logging
from logging import handlers

# BOILERPLATE
# TODO: Use Function
# TODO: Use lib (loguru)

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# New Instance
log = logging.Logger("Fabio", log_level)

# Set Level
#ch = logging.StreamHandler() # Console/Terminal/stderr
#ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=10**6, # Recommend 10**6
    backupCount=10,
)
fh.setLevel(log_level)

# Format
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)

# ch.setFormatter(fmt)
fh.setFormatter(fmt)

# Destiny
# log.addHandler(ch)
log.addHandler(fh)

'''
log.debug("Msg for Dev, QA, SYSAdmin")
log.info("General Msg for Users")
log.warning("Warning msg that doesn't cause errors")
log.error("Errors that only afect a unique execution")
log.critial("General Error, e.g.: Database error")
'''

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("%s", str(e))