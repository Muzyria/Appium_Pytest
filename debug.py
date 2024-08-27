
def parameterized_decorator(param):
    def decorator(func):
        def inner(*args, **kwargs):
            print(f"--------------------------------- {param}")
            func(*args, **kwargs)
        return inner
    return decorator


text = "TEST"


@parameterized_decorator(text)
def my_func(device: str):
    print(f"--{device}--")


my_func(text)

