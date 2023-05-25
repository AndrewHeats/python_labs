from sys import exception


def write_dictionary_of_kwargs(func):
    def wrapper(*args, **kwargs):
        file_path = "D:/python_labs/Zoo/files/Aattr.txt"
        with open(file_path, "a") as file:
            func_name = func.__name__
            arguments = ", ".join(f"{key}={value}" for key, value in kwargs.items())
            line = f"{func_name}: {arguments}\n"
            file.write(line)
        return func(*args, **kwargs)

    return wrapper


def exception_writer(func):
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
