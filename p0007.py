import sys

from util import prime_generator

def nth_prime(n: int):
    for i, prime in enumerate(prime_generator(sys.maxsize), start=1):
        if i == n:
            return prime

def main():
    print(f'The 10001th prime is {nth_prime(10001)}')

if __name__ == '__main__':
    main()