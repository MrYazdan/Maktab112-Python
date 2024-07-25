import logging

# from builtins import print as base_print

# print = lambda *args, **kwargs: base_print("LOGGER: ", *args, **kwargs)
# print("maktab", 112, sep=":")

# Logging Levels:
# -----------------------------------------------------------------------------------------
#  level name | level |            Usage             |       Example
# -----------------------------------------------------------------------------------------
#    DEBUG    |  10  | Debug information, Diagnosing | Trace program ...
#    INFO     |  20  |   (SOFT) Soft log, Detail     | OS Space
#   WARNING   |  30  |    warning ! => warnings !    | Disk space low ...
#    ERROR    |  40  | to log normal issues (errors) | Invalid Data
#   CRITICAL  |  50  | to log high importance issues | Internet connection, Application STOP
#    FATAL    |  50  | to log high importance issues | Attacks, Hijack
# ------------------------------------------------------------------------------------------

# Basic Level
# logging.basicConfig(level=logging.ERROR)
# logging.basicConfig(level=0)
# logging.basicConfig(level=logging.WARN)

# custom formatting:
custom_logger_format = "%(asctime)s | %(name)s | %(levelname)s: %(message)s "
# logging.basicConfig(level=0, format=custom_logger_format)

# Tests:
# logging.log(logging.DEBUG, "A Debug log")
# logging.debug("A Debug log")
#
# logging.log(logging.INFO, "A Info log")
# logging.info("A Info log")
#
# logging.log(logging.WARN, "A Warning log")
# logging.warning("A Warning log")
#
# logging.log(logging.ERROR, "A Error log")
# logging.error("A Error log")
#
# logging.log(logging.CRITICAL, "A Critical log")
# logging.critical("A Critical log")
#
# logging.log(logging.FATAL, "A Fatal log")
# logging.fatal("A Fatal log")


# Create new logger:
logger = logging.getLogger("maktab")
logger.setLevel(10)

formatter = logging.Formatter(custom_logger_format)
error_formatter = logging.Formatter("%(asctime)s | %(lineno)d | %(message)s")

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(0)

file_handler = logging.FileHandler("errors.logs", "a", "utf-8")
file_handler.setFormatter(error_formatter)
file_handler.setLevel(logging.ERROR)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("A Debug log")
logger.info("A Info log")
logger.warning("A Warning log")
logger.error("A Error log")
logger.critical("A Critical log")
logger.fatal("A Fatal log")
