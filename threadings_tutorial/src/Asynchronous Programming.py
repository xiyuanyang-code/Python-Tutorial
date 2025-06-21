import asyncio


async def say_hello():
    print("Hello")
    # the simulation of IO process
    await asyncio.sleep(1)
    print("World")


asyncio.run(say_hello())
