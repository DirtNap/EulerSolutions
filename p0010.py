from util import prime_generator

def main():
    result = 0
    for pn in prime_generator(2000000):
        result += pn
    print(f'The sum of prime numbers below 2000000 is {result}')

if __name__ == '__main__':
    main()