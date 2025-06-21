import time
import requests
import asyncio
import aiohttp

urls = [
    "https://github.com",
    "https://sjtu.edu.cn",
    "https://acm.sjtu.edu.cn/OnlineJudge/",
    "https://chat.deepseek.com/",
    "https://www.bilibili.com/",
    "https://stackoverflow.com/questions"
]


def fetch_url_simple(url):
    try:
        response = requests.get(url, timeout=10)  # 设置超时时间为 10 秒
        return response.text
    except requests.exceptions.Timeout:
        print(f"Timeout occurred while fetching {url}")
        return ""
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error occurred: {e}")
        return ""
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return ""


def test_for_simple():
    # Using the for-loop
    for url in urls:
        content = fetch_url_simple(url)
        print(f"{url} returns {len(content)} bytes")


async def fetch_url(url):
    timeout = aiohttp.ClientTimeout(total=10)  # 设置超时时间为 10 秒
    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as response:
                return await response.text()
    except asyncio.TimeoutError:
        print(f"Timeout occurred while fetching {url}")
        return ""


async def test_for_concurrency():
    """: The test for fetching urls: test for concurrency"""
    # Task list
    tasks = [fetch_url(url) for url in urls]

    # For all tasks: Concurrency
    results = await asyncio.gather(*tasks)

    for url, content in zip(urls, results):
        print(f"{url} returns {len(content)} bytes")


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(test_for_concurrency())
    end_time = time.time()
    print(f"Total time for concurrency: {end_time - start_time:.2f} seconds")

    start_time = time.time()
    test_for_simple()
    end_time = time.time()
    print(f"Total time for no concurrency: {end_time - start_time:.2f} seconds")
