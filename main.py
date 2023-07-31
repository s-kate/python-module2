def is_num_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


def prime_generator():
    num = 2
    while True:
        if is_num_prime(num):
            yield num
        num += 1


prime_gen = prime_generator()
for ii in range(10):
    print(next(prime_gen))
