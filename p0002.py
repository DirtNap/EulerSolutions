import typing

from util import fibonacci_generator

def fibonacci_sum(limit: int, filter: typing.Callable=lambda x: True):
    result = 0
    for current in fibonacci_generator(limit):
        if filter(current):
            result += current
    return result

def main():
    print(f'The sum of even fibonacci numbers less than 4000000 is {fibonacci_sum(4000000, lambda x: x % 2 == 0)}')

if __name__ == '__main__':
    main()