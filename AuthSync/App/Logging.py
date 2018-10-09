import os
import sys
import logging


class InfoFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno in (logging.DEBUG, logging.INFO)


# Look into doing log rollover every 24 hours

class Logging:
    def __init__(self, name):
        self.__logger = logging.getLogger(name)
        LogLevel = getattr(logging, str(os.getenv('LOG_LEVEL', 'info')).upper())
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # STDOUT Info / Debug
        h1 = logging.StreamHandler(sys.stdout)
        h1.setLevel(logging.DEBUG)
        h1.addFilter(InfoFilter())
        h1.setFormatter(formatter)

        # STDERR Warning / Error
        h2 = logging.StreamHandler(sys.stderr)
        h2.setLevel(logging.WARNING)
        h2.setFormatter(formatter)

        # Assign logging handlers
        self.__logger.addHandler(h1)
        self.__logger.addHandler(h2)

        self.setlevel(LogLevel)

    def setlevel(self, level=logging.DEBUG):
        self.__logger.setLevel(level)
        pass

    def critical(self, msg, *args, **kwargs):
        self.__logger.critical(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.__logger.error(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.__logger.warning(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.__logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self.__logger.debug(msg, *args, **kwargs)
