import asyncio
import time
from util import async_timed
# time.sleep(1)

@async_timed
async def main():
    start = time.time()
    print('hello')
    # 协程必须要等待，也就是必须在前面加上await
    await asyncio.sleep(1)
    # 在协程中，对于那些会发生阻塞的I/O代码，一定不要使用同步的，否则程序会阻塞在这个同步代码，市区并发行
    print('world')
    end = time.time();
    ok = end - start
    print(ok)
    
if __name__ == '__main__':
    # main()：创建一个协程，并不是直接运行main函数，并且这个协程是不会自己运行的
    cor = main()
    # 要把协程丢到事件循环中才会执行
    asyncio.run(cor)
