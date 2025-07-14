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
        # asyncio.timeout_at(2)
        async with asyncio.timeout(2):
            task1 = await asyncio.create_task(greet('xx', 1))
            task2 = await asyncio.create_task(greet('yy', 3))

            result1 = await task1
            print(result1)
            result2 = await task2
            print(result2)
    except asyncio.TimeoutError:
        print('timeout')
        task = asyncio.all_tasks()
        print(task)

if __name__ == '__main__':
    asyncio.run(main())
