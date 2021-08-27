def multiple_sum(limit, *multiples):
    result = 0
    current = 1
    while current < limit:
        if not all((current % m for m in multiples)):
            result += current
        current += 1
    return result

def main():
    print(f'The sum of multiples of 3 and 5 less than 1000 is {multiple_sum(1000, 3, 5)}')

if __name__ == '__main__':
    main()