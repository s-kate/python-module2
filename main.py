def log_func(func):
    print('Hello, world')
    func()
    print('Goodbye, world')


@log_func
def my_func():
    print(5 * 6)

