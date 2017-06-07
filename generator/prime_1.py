import math

def is_prime(number):
    if number >1:
        if number == 2:
            return True
        if number %2 == 0:
            return False
        for curr in range(3, int(math.sqrt(number)+1), 2):
            if number % curr == 0:
                return False
        return True
    return False


def get_primes(number):
    while True:
        if is_prime(number):
            print(number)
            yield number
        number += 1


def solve_number_10():
    for next_prime in get_primes(0):
        if next_prime < 100:
            print(next_prime)
        else:
            return

solve_number_10()