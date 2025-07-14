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

async_timed
async def main1():
    # 如果这个协程超时了，就无法再继续运行了
    try:
        result = await asyncio.wait_for(greet('xx', 2), timeout=1)
        print(result)

    except asyncio.TimeoutError:
        print('timeout')
        tasks = asyncio.all_tasks()
        for task in tasks:
            print(task.get_name())


async_timed
async def main():
    aws = [
        asyncio.create_task(greet_group('xx', 1)),
        asyncio.create_task(greet('yy', 2)),
        asyncio.create_task(greet('zz', 3)),
        asyncio.create_task(greet('aa', 4)),
        asyncio.create_task(greet('bb', 5)),
        asyncio.create_task(greet('cc', 6)),
        asyncio.create_task(greet('dd', 7)),

    ]
    # 返回一个元组（执行完成的任务，执行超时的任务）
    # 如果未指定timeout，永远不会超时
    done_tasks, pending_tasks = await asyncio.wait(aws, timeout=2, return_when=asyncio.FIRST_COMPLETED)
    print(done_tasks)
    print(pending_tasks)

    for task in pending_tasks:
        result = await task
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
