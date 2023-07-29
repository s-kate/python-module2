def square_generator(number: int):
    count = 1
    while number >= count:
        yield count ** 2
        count += 1


for square in square_generator(5):
    print(square)
