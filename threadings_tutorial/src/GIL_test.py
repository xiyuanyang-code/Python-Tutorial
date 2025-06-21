import threading
import time
import multiprocessing


def cpu_task(n: int):
    """simulation of CPU intensive task

    Args:
        n (int): the total count steps
    """
    while n > 0:
        n -= 1
    print("CPU task ends")


def io_task():
    """simulation of IO-intensive task"""
    time.sleep(1)


def test_task_cpu(task_function):
    """test for GIL in CPU-intensive task"""
    print("Test for CPU-intensive task:")
    print("Test for single threaded:")
    start_time = time.time()
    task_function(500_000_000)
    end_time = time.time()
    print(f"Single-threaded execution time: {end_time - start_time:.2f} seconds")

    print("Test for multi threaded:")
    start_time = time.time()
    t1 = threading.Thread(target=task_function, args=(250_000_000,))
    t2 = threading.Thread(target=task_function, args=(250_000_000,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.time()
    print(f"Multi-threaded execution time: {end_time - start_time:.2f} seconds")


def test_task_io(task_function):
    print("\nTest for Io-intensive task:")
    # single threads:
    start_time = time.time()
    for _ in range(10):
        io_task()
    end_time = time.time()
    print(f"Single-threaded execution time: {end_time - start_time:.2f} seconds")

    threads = [threading.Thread(target=io_task) for _ in range(10)]
    start_time = time.time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end_time = time.time()
    print(f"Multi-threaded execution time: {end_time - start_time:.2f} seconds")


def multiprocess_cpu_task():
    print("Using multi-processing")
    start_time = time.time()
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=cpu_task, args=(100_000_000,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    end_time = time.time()
    print(f"All processes finished, time: {end_time - start_time:.2f}")


if __name__ == "__main__":
    test_task_cpu(cpu_task)
    # test_task_io(io_task)
    multiprocess_cpu_task()
