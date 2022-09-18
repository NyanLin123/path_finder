import time
from functools import wraps


def timethis(func):
    '''
    report these conversation
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


@timethis
def countdown(n: int):
    ''' 
    name result 
    '''
    while n > 0:
        n -= 1


print(countdown.__annotations__)
print(countdown.__doc__)
