from typing import Callable
from functools import wraps
import time
import random


def lead_time(fun: Callable):
    
    @wraps(fun)
    def wraper(*args, **kwargs):
        prev_time = time.time()
        result = fun(*args, **kwargs)
        print(f"[INFO]: Lead time: {time.time() - prev_time}")
        return result

    return wraper

def lead_time_multiple(count: int, fun: Callable, data) -> None:
    prev_time = time.time()
    for _ in range(count):
        fun(data)
    print(f'[Lead time]: {time.time() - prev_time}')