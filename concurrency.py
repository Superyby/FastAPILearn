import asyncio
from util import async_timed


async def greet(name, dalay):
    await asyncio.sleep(dalay)
    return f'hello {name}'


# 1.用创建任务的方式并发运行
@async_timed
async def main():
    # 并发执行，必须包装成Task对象 以下是正确写法
    # 注意，必须要把所有任务创建好，再分别await，才能并发运行
    task1 = asyncio.create_task(greet('xx',1))
    task2 = asyncio.create_task(greet('yy',2))
    
    # 对创建好的任务await
    result1 = await task1
    print(task1)
    result2 = await task2
    print(task2)
    
    # # 以下是错误写法
    # result1 = await asyncio.create_task(greet('xx',1))
    # result2 = await asyncio.create_task(greet('yy',2))

# 这是同步执行
# @async_timed
# async def main():
#     result1 = await greet('xx', 1)
#     print(result1)
#     result2 = await greet('yy', 2)
#     print(result2)
    
if __name__ == '__main__':
    asyncio.run(main())