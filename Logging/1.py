import logging

# when a module is imported the code from the module is run

# FOUR LOGGING LEVELS
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL
#
#
# By default warning level is set to WARNING i.e. anything above(ERROR, CRITICAL) that and WARNING are logged

# logging.DEBUG is just a integer constant in the backend
# logging.basicConfig(level=logging.DEBUG) # this will only print log statements to the terminal

# to put logs in a file
# logging.basicConfig(filename="test.log", level=logging.DEBUG)

# to change the format of the log
# log attribute docs = https://docs.python.org/3/library/logging.html#logrecord-attributes
logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


def add(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


def mul(a: int, b: int) -> int:
    return a * b


def div(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError
    return a / b


def main():
    logging.debug(f"1 + 2 = {add(1, 2)}")
    logging.debug(f"1 - 2 = {sub(1, 2)}")
    logging.debug(f"1 * 2 = {mul(1, 2)}")
    logging.debug(f"1 / 2 = {div(1, 2)}")


if __name__ == "__main__":
    main()
