import datetime
import time


def rate_limit(max_calls, period):

    def decorator(func):

        def rating(*args, **kwargs):
            calls = 0
            now = datetime.datetime.now()
            print(now)
            window_start = now - datetime.timedelta(seconds=period)

            return func(*args, **kwargs)

        return rating
    return decorator


@rate_limit(3, 4)
def printing():
    time.sleep(1)
    return 'Hello, world!'


print(printing())
print(printing())
print(printing())
print(printing())
