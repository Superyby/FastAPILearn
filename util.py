from functools import wraps
import time


def async_timed(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        print(f"开始执行{func}，参数：{args},{kwargs}")
        start = time.time()
        try:
            return await func(*args, **kwargs)
        finally:
            end = time.time()
            totle = end - start
            print(f"结束执行{func}，耗时:{totle: .4f}")
    return wrapper
