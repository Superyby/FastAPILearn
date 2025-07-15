from util import async_timed
import asyncio
# import time
from functools import partial


async def task_will_fail():
    await asyncio.sleep(1)
    raise ValueError('This task will fail')
# exception方法
# @async_timed
async def main1():
    # create_task创建任务后，这个任务会立马加入到事件循环中调度
    task = asyncio.create_task(task_will_fail())
    await asyncio.sleep(2)
    print(task.exception())

# 回调
def my_callback(future, tag):
    print('='*30)
    print(type(future))   # 传函数，加括号是传结果
    # 获取任务返回值
    print(future.result())
    print(tag)
    print('='*30)


async def greet(name, dalay):
    await asyncio.sleep(dalay)
    return f'hello {name}'


async def main2():
    task = asyncio.create_task(greet('xx', 2))
    # partial:偏函数，可以将这个函数提前准备好一些参数
    task.add_done_callback(partial(my_callback, tag='tag'))
    await task
    
    
# 取消
async def something():
    print('something else')
    await asyncio.sleep(15)
    
async def main():
    task = asyncio.create_task(something(),name='ok')
    await asyncio.sleep(1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print('是否已取消', task.cancelled())

if __name__ == '__main__':
    asyncio.run(main())
