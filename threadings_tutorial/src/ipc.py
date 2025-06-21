from multiprocessing import Process, Queue, Pipe
import multiprocessing
import multiprocessing.connection
import os


def worker_queue(q: Queue):
    print(f"PID2: {os.getpid()}")
    q.put("Hello from child process")
    print(f"Message sent from subprocess: {os.getpid()}")


def worker_pipe(conn: multiprocessing.connection.Connection):
    print(f"PID2: {os.getpid()}")
    conn.send("Message from child")
    print(f"Message sent from subprocess: {os.getpid()}")
    conn.close()


def test_pipe():
    parent_conn, child_conn = Pipe()
    print(f"PID1: {os.getpid()}")
    p = Process(target=worker_pipe, args=(child_conn,))
    p.start()
    print(f"Message received to {os.getpid()}: {parent_conn.recv()}")
    p.join()


def test_queue():
    q = Queue()
    p = Process(target=worker_queue, args=(q,))
    print(f"PID1: {os.getpid()}")
    p.start()
    print(f"Message received to {os.getpid()}: {q.get()}")
    p.join()


if __name__ == "__main__":
    test_pipe()
    test_queue()
