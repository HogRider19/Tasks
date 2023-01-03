from typing import Callable
from functools import wraps
import time


def lead_time(fun: Callable):
    
    @wraps(fun)
    def wraper(*args, **kwargs):
        prev_time = time.time()
        result = fun(*args, **kwargs)
        print(f"[INFO]: Lead time: {time.time() - prev_time}")
        return result

    return wraper