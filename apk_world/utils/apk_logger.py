import logging


def print_and_log(massage, default_level="debug", **kwargs):

    if default_level == "debug":
        logger.debug(massage)

    elif default_level == "info":
        logger.info(massage)

    elif default_level == "critical":
        logger.critical(massage)

    elif default_level == "error":
        logger.error(massage)

    if kwargs and "func" in kwargs:
        kwargs["func"](kwargs)

    print(massage, **kwargs)

logger = logging.getLogger(__name__)
