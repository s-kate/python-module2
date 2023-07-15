def even_odd_generator(num: int):
    i = 1
    while num >= i:
        if i % 3 == 0 and i % 5 == 0:
            yield 'FizzBuzz'
        elif i % 3 == 0:
            yield 'Fizz'
        elif i % 5 == 0:
            yield 'Buzz'
        else:
            yield i
        i += 1


for el in even_odd_generator(15):
    print(el)
