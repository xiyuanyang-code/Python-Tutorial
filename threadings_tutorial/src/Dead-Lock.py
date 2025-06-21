import threading

lock_a = threading.Lock()
lock_b = threading.Lock()


def thread_1():
    with lock_a:
        print("Thread 1 acquired lock A")
        with lock_b:
            print("Thread 1 acquired lock B")

    print("Finished!")


def thread_2():
    with lock_b:
        print("Thread 2 acquired lock B")
        with lock_a:
            print("Thread 2 acquired lock A")

    print("Finished!")


def thread_1_timeout():
    if lock_a.acquire(timeout=2):
        print("Thread 1 acquired lock A")
        try:
            if lock_b.acquire(timeout=2):
                print("Thread 1 acquired lock B")
                print("Thread 1 finished!")
            else:
                print("Thread 1 could not acquire lock B, releasing lock A")
        finally:
            lock_a.release()
    else:
        print("Thread 1 could not acquire lock A")


def thread_2_timeout():
    if lock_b.acquire(timeout=2):
        print("Thread 2 acquired lock B")
        try:
            if lock_a.acquire(timeout=2):
                print("Thread 2 acquired lock A")
                print("Thread 2 finished!")
            else:
                print("Thread 2 could not acquire lock A, releasing lock B")
        finally:
            lock_b.release()
    else:
        print("Thread 2 could not acquire lock B")


t1 = threading.Thread(target=thread_1_timeout)
t2 = threading.Thread(target=thread_2_timeout)
t1.start()
t2.start()
t1.join()
t2.join()
