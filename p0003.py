import math

from util import prime_generator

def largest_prime_factor(target: int) -> int:
    result = 0
    limit = int(math.sqrt(target)) + 1

    for current in prime_generator(limit):
        if target % current == 0:
            result = current
    return result


def main() -> None:
    print(f'The largest prime factor of 600851475143 is {largest_prime_factor(600851475143)}')

if __name__ == '__main__':
    main()