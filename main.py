def memoize():

    def decorator(func):

        def memory(*args, **kwargs):
            cache = {}
            key = args + kwargs
            for key in cache:
                return cache[key]

            new_result = func(*args, **kwargs)
            cache[key] = new_result
            return new_result

        return memory
    return decorator
