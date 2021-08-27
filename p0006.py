import typing

def sum_square_difference(count: int) -> typing.Tuple[int, int, int]:
    base = 0
    sum_sq = 0
    for num in range(1, count + 1):
        base += num
        sum_sq += num * num
    exp = base ** 2
    return exp, sum_sq, max(exp, sum_sq) - min(exp, sum_sq)

def main() -> None:
    exp, sum_sq, diff = sum_square_difference(100)
    print(f'The difference between the square of sums ({exp}) and sum of squares ({sum_sq}) of the first 100 numbers is {diff}')

if __name__ == '__main__':
    main()