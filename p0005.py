import math
def least_common_multiple(upper_limit: int) -> int:
    result = 1
    for current in range(1, upper_limit + 1):
        if result % current != 0:
            result = math.lcm(result, current)
    return result

def main() -> None:
    print(f'The smallest number which has all factors less than 20 is {least_common_multiple(20)}')

if __name__ == '__main__':
    main()