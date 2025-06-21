import multiprocessing
import os


def worker(num):
    print(f"Worker {num} running in process {os.getpid()}")
    return


if __name__ == "__main__":
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    print("All processes finished")
