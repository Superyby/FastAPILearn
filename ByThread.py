from util import async_timed
import asyncio
import time

def get_url(url):
    print(f"开始获取{url}")
    time.sleep(2)
    print(f"完成获取{url}")
    return "success"

async def greet(name, dalay):
    await asyncio.sleep(dalay)
    return f'hello {name}'

@async_timed
async def main():
    result = await asyncio.gather(
        # get_url("www.baidu.com"),
        asyncio.to_thread(get_url,url="www.baidu.com"),
        greet("urzzl2",2),
        # get_url("url3"),
    )
    print(result)

if __name__ == '__main__':
    asyncio.run(main())