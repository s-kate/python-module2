import time


def timeit(func):
    start_time = time.time()
    func()
    end_time = time.time()
    total_time = end_time - start_time
    print(f'total time: {total_time}')


@timeit
def sleep():
    time.sleep(3)

