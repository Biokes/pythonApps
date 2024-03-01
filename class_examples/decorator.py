from time import time


def decorator(fn):
    def inner_fn(*args, **kwargs):
        print("whatever u want should be here")
        print(fn(*args, **kwargs))
        print("whatever u want should be here")

    return inner_fn


def execution_time(func):
    def wrap(*args, **kwargs):
        time_started = time()
        result = func()
        time_ended = time()
        return f"it took {time_ended - time_started:.2f}secs to execute this function"

    return wrap


@decorator
@execution_time
def loop(numbers: int):
    return_list = []
    for number in range(numbers):
        return_list.append(number)
    return numbers.__str__()


loop(2)
print()
