from contextlib import contextmanager


class Divider:

    def __init__(self, symbol='/'):
        self.symbol = symbol

    def __enter__(self):
        print(self.symbol)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.symbol)


with Divider():
    print('hello, world')


# or


@contextmanager
def divider(symbol='='):
    print(symbol)
    yield
    print(symbol)


with divider('*'):
    print('Hello world!')
