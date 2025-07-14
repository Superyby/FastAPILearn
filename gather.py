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
        # 队列
        result = await asyncio.gather(
            greet_group('xx', 1),
            greet('yy', 2),
            # return_exceptions=True
        )
    except Exception as e:
        pass
    tasks = asyncio.all_tasks()
    for task in tasks:
        # Task-1代表main线程，不能await自身
        if task.get_name() == 'Task-1':
            continue
        # 说明gather中即使有任务发生异常，剩余没执行完的任务也不会取消
        # print(task.get_name(),task.cancelled())
        result = await task
        print(result)

if __name__ == '__main__':
    asyncio.run(main())
