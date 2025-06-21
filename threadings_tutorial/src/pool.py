from multiprocessing import Pool

def worker(x):
    return x * x

if __name__ == '__main__':
    with Pool(processes=4) as pool: 
        # 同步执行
        result = pool.apply(worker, (10,))
        print(result)  # 输出: 100
        
        # 异步执行
        result = pool.apply_async(worker, (20,))
        print(result.get())  # 输出: 400
        
        # map方法
        results = pool.map(worker, range(10))
        print(results)  # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        
        # imap方法(惰性求值)
        for res in pool.imap(worker, range(5)):
            print(res)  # 依次输出: 0, 1, 4, 9, 16