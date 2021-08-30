import typing
def pythagorean_triplet_by_sum(target_sum: int) -> typing.Union[typing.Tuple[int, int, int], typing.Tuple[None, None, None]]:
    for a in range(1, target_sum - 2):
        for b in range(a, target_sum - a):
            c = target_sum - (a + b)
            if any((a > c, b > c)):
                break
            if a ** 2 + b ** 2 == c ** 2:
                return a, b, c
    return None, None, None

def main():
    a, b, c = pythagorean_triplet_by_sum(1000)
    if a is None:
        print('No Pythagorean Triplet exists whose sum is 1000.')
    else:
        print(f'The product of the Pythagorean Triplet whose sum is 1000 ({a}, {b}, {c}) is {a * b * c}.')

if __name__ == '__main__':
    main()
