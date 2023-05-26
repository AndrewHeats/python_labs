"""
This is a file which contains decorators
"""


# pylint: disable = unspecified-encoding
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
            raise
        return result

    return wrapper
