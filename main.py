def retry(num):

    def decorator(func):

        def retries(*args, **kwargs):
            for i in range(num):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    pass
            raise Exception(f'Function failed after {num} tries.')

        return retries
    return decorator


@retry(3)
def example(a, b):
    return a / b


print(example(23, 0))
