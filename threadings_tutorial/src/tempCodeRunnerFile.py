p = Process(target=worker, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())  # 输出: Message from child
#     p.join()
# if __name__ == "__main__":
#     q = Queue()
#     p = Process(target=worker, args=(q,))
#     print(f"PID1: {os.getpid()}")
#     p.start()
#     print(f"Message received to {os.getpid()}: {q.get()}")
#     p.join()
