import itertools
from util import is_palindrome

def main() -> None:
    three_digit_nums = list(range(999, 99, -1))
    current = 0
    for product in (x * y for (x, y) in itertools.combinations_with_replacement(three_digit_nums, 2)):
        if product > current and is_palindrome(str(product)):
            current = product
    print(f'The largest palindromic product of three digit numbers is {current}')

if __name__ == '__main__':
    main()