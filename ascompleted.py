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
    aws = [
        greet_group('xx', 1),
        greet('yy', 2),
        greet('zz', 3)
    ]
    try:
        for corn in asyncio.as_completed(aws):
            result = await corn
            print(result)
    except Exception as e:
        pass
    tasks = asyncio.all_tasks()
    for task in tasks:
        print(task.get_name(), task.cancelled())
        if task.get_name() != 'Task-1':
            result = await task
            print(result)
        

if __name__ == '__main__':
    asyncio.run(main())
