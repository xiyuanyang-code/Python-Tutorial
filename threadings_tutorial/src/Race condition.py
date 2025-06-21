import threading
import time

# Shared variables for threadings
balance = 100

# lock object
lock = threading.Lock()


def withdraw(amount):
    global balance
    if balance >= amount:
        time.sleep(1)
        print(f"Getting money..., the amount is {amount}")
        balance -= amount
        print(f"Get {amount}, {balance} remaining...")
    else:
        print("Error! You don't have enough money!")


def withdraw_with_locked(amount):
    global balance
    with lock:
        if balance >= amount:
            time.sleep(1)
            print(f"Getting money..., the amount is {amount}")
            balance -= amount
            print(f"Get {amount}, {balance} remaining...")
        else:
            print("Error! You don't have enough money!")


def test_thread_safe():
    """test for race condition, safe mode for entering in queue"""
    print("If they take turns to withdraw money at the counter in order.")
    t1 = threading.Thread(target=withdraw, args=(80,))
    t2 = threading.Thread(target=withdraw, args=(70,))
    t3 = threading.Thread(target=withdraw, args=(50,))
    t4 = threading.Thread(target=withdraw, args=(20,))

    # Starting multi-sessions, in queue
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()
    t4.start()
    t4.join()


def test_thread_unsafe():
    """test for race condition, unsafe mode for multithreads"""
    print("If the four of them withdraw money at the counter simultaneously...")
    t1 = threading.Thread(target=withdraw, args=(80,))
    t2 = threading.Thread(target=withdraw, args=(70,))
    t3 = threading.Thread(target=withdraw, args=(50,))
    t4 = threading.Thread(target=withdraw, args=(20,))

    # Starting multi-sessions
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()


def test_thread_unsafe_with_locked():
    """test for race condition, unsafe mode for multithreads, but with lock"""
    print("If the four of them withdraw money at the counter simultaneously..., but with lock😋!")
    t1 = threading.Thread(target=withdraw_with_locked, args=(80,))
    t2 = threading.Thread(target=withdraw_with_locked, args=(70,))
    t3 = threading.Thread(target=withdraw_with_locked, args=(50,))
    t4 = threading.Thread(target=withdraw_with_locked, args=(20,))

    # Starting multi-sessions
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()


if __name__ == "__main__":
    # test for safe single-thread
    test_thread_safe()

    # reset balance
    balance = 100

    # test for race condition: multithreads
    test_thread_unsafe()

    balance = 100

    # test with lock
    test_thread_unsafe_with_locked()
