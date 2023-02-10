import logging
import time
from functools import lru_cache, wraps

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")


# Basic Decorators
def logger_decorator(orig_func):
    def wrapper_func(*args, **kwargs):
        """This is logger_decorator's wrapper func"""
        logging.info(f"Function name: {orig_func.__name__}")
        return orig_func(*args, **kwargs)

    return wrapper_func


def another_decorator(orig_func):
    def wrapper_func(*args, **kwargs):
        """This is another_decorator's wrapper func"""
        logging.info("Inside another decorator func")
        return orig_func(*args, **kwargs)

    return wrapper_func


# Timeit decorators
def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """This is timeit's wrapper func"""
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds to complete")
        return result

    return wrapper


# Call Count
def countcall(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(f"{func.__name__} has been called {wrapper.count} times")
        return result

    wrapper.count = 0
    return wrapper


@another_decorator
@logger_decorator
def plus_two_number(a, b):
    """This is plus_two_number function"""
    return a + b


@timeit
@countcall
@lru_cache  # LRU Cache
def add_two_number(a, b):
    """This is add_two_number function"""
    return a + b


if __name__ == "__main__":
    result = plus_two_number(1, 2)

    # @wraps(orig_func):
    print(
        plus_two_number.__name__, plus_two_number.__doc__
    )  # wrapper_func instead of plus_two_number
    print(
        add_two_number.__name__, add_two_number.__doc__
    )  # add_two_number This is add_two_number function since we use @wraps()

    # @lru_cache: When calling the input function,
    #   it first checks if its arguments are present in the cache.
    #   If it’s the case, return the result.
    #   Otherwise, compute it and put it in the cache
    add_two_number(1000, 999)  # call the 1st time same input
    add_two_number(1000, 999)  # call the 2nd time same input
    add_two_number(1000, 999)  # call the 3rd time same input
