import time
from contextlib import contextmanager

class Timer:

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        total_time = self.end_time - self.start_time
        print(f'total time: {total_time}')


with Timer():
    time.sleep(5)


# or


@contextmanager
def timer():
    start_time = time.time()
    yield
    end_time = time.time()
    total_time = end_time - start_time
    print(f'total time: {total_time}')


with timer():
    time.sleep(3)
