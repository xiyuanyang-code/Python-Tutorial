import time
import asyncio
import random


def user_io_simulation():
    """Use time.sleep to simulate the wait for user input"""
    time.sleep(2)
    return random.randint(1, 5)


def simulation():
    total = 100
    while total > 0:
        total -= 1
        if total % 20 == 0:
            input = user_io_simulation()
            print(f"User enters the input {input}")
            total -= input
        print(f"Now the total value is {total}")
    print("Done!")

async def user_io_simulation_2():
    """Simulation with async

    Returns:
        int: The user input
    """
    await asyncio.sleep(2)
    return random.randint(1, 5)


async def simulation_concurrency():
    total = 100
    tasks = []  # List to store tasks
    while total > 0:
        total -= 1
        if total % 20 == 0:
            # Create a task for user input simulation
            task = asyncio.create_task(user_io_simulation_2())
            tasks.append(task)
        print(f"Now the total value is: {total}")

    # Wait for all tasks to complete
    results = await asyncio.gather(*tasks)
    for user_input in results:
        print(f"User enters the input: {user_input}")
        total -= user_input

    print("Done!")
    return 0


async def main():
    await simulation_concurrency()


if __name__ == "__main__":
    print("Testing simulation for no concurrency")
    start_time = time.time()
    simulation()
    end_time = time.time()
    print(f"Time cost: {end_time - start_time:.2f} seconds")

    print("Testing simulation for concurrency")
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"Time cost: {end_time - start_time:.2f} seconds")

