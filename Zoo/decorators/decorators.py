"""
This is a file which contains decorators
"""
import logging
from functools import wraps


# pylint: disable = unspecified-encoding
# pylint: disable = raise-missing-from
# pylint: disable = broad-exception-caught
# pylint: disable = inconsistent-return-statements
def write_dictionary_of_kwargs(func):
    """
    This is decorator which write to file
    dictionary of key value arguments
    :param func:
    :return: func
    """

    def wrapper(*args, **kwargs):
        file_path = "D:/python_labs/Zoo/files/Aattr.txt"
        with open(file_path, "a") as file:
            func_name = func.__name__
            file.write(func_name)
            file.write(": ")
            for key, value in kwargs.items():
                arguments = f"{key} = {value}"
                line = f"{arguments},"
                file.write(line)
            file.write("\n")
        return func(*args, **kwargs)

    return wrapper


def exception_writer(func):
    """
        This is decorator which write to file
        exception and method in which this exception cause
        :param func:
        :return: func
        """

    def wrapper(*args, **kwargs):
        file_path = "D:/python_labs/Zoo/files/ex.txt"
        try:
            result = func(*args, **kwargs)
        except Exception as exc:
            with open(file_path, 'a') as file:
                file.write(f"Method: {func.__name__}, Exception: {type(exc).__name__}\n")
            raise exc
        return result

    return wrapper


def logged(exception, mode):
    """
    This is decorator which write exceptions to file or
    print in console
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as exc:
                logger = logging.getLogger()
                if mode == "console":
                    logger.addHandler(logging.StreamHandler())
                elif mode == "file":
                    logger.addHandler(logging.FileHandler("log.txt"))
                logger.exception(exc)

        return wrapper

    return decorator
