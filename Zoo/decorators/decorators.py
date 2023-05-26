"""
This is a file which contains decorators
"""


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
            file.write(":\n")
            for k, v in kwargs.items():
                arguments = f"{k} = {v}"
                line = f"{arguments}\n"
                file.write(line)
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
        except Exception as e:
            with open(file_path, 'a') as file:
                file.write(f"Method: {func.__name__}, Exception: {type(e).__name__}\n")
            raise
        else:
            return result

    return wrapper
