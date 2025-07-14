from util import async_timed
import asyncio


async def greet(name, dalay):
    await asyncio.sleep(dalay)
    return f'hello {name}'

async def greet_group(name, dalay):
    if name == 'xx':
        raise ValueError('xx is not allowed') 
    await asyncio.sleep(dalay)
    return f'hello {name}'

@async_timed
async def main():
    try:
        async with asyncio.TaskGroup() as group:
            # 在这里创建任务就不需要asyncio.create_task()
            task1 = group.create_task(greet_group('xx',1))
            task2 = group.create_task(greet_group('yy',2))
            task3 = group.create_task(greet_group('zz',3))
    except Exception as e:
        print(e)
    # 上面代码执行后有两种情况
    # 1. 所有任务执行完成 2. 有异常
    # print(task1.result())
    # print(task2.result())
    print(task1.done())
    print(task2.cancelled())
    print(task3.cancelled())

if __name__ == '__main__':
    asyncio.run(main())