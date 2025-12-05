import logging

# else after try execpt blocks

logger = logging.getLogger(__name__)  # to get a custom logger (default is root)

# logging levels can be set at the logger level but handlers can override this
logger.setLevel(logging.DEBUG)

# defining a custom a log format
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")

# custom log handlers for console and file
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("test1.log")

# formatters have to be added to handlers
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# handlers can override log levels of the logger
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.INFO)

# handlers have to be connected to the loggers
logger.addHandler(stream_handler)
logger.addHandler(file_handler)


def add(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


def mul(a: int, b: int) -> int:
    return a * b


def div(a: int, b: int) -> float | None:
    try:
        return a / b
    except Exception as e:
        logger.critical("divide by zeror error : ", e)


def main():
    logger.debug(f"1 + 2 = {add(1, 2)}")
    logger.debug(f"1 - 2 = {sub(1, 2)}")
    logger.debug(f"1 * 2 = {mul(1, 2)}")

    logger.info(f"1 + 2 = {add(1, 2)}")
    logger.info(f"1 - 2 = {sub(1, 2)}")
    logger.info(f"1 * 2 = {mul(1, 2)}")

    logger.warning(f"1 + 2 = {add(1, 2)}")
    logger.warning(f"1 - 2 = {sub(1, 2)}")
    logger.warning(f"1 * 2 = {mul(1, 2)}")

    logger.error(f"1 + 2 = {add(1, 2)}")
    logger.error(f"1 - 2 = {sub(1, 2)}")
    logger.error(f"1 * 2 = {mul(1, 2)}")

    logger.critical(f"1 + 2 = {add(1, 2)}")
    logger.critical(f"1 - 2 = {sub(1, 2)}")
    logger.critical(f"1 * 2 = {mul(1, 2)}")

    # to include the traceback
    logger.exception(div(1, 0))


if __name__ == "__main__":
    main()
