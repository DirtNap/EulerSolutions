import collections
def prime_generator(upper_limit: int, start: int=2):
    """Generate a list of prime numbers, starting with start, which are less than upper_limit."""
    found = collections.defaultdict(list)
    current = start
    while current < upper_limit:
        if current in found:
            for factor in found[current]:
                found[factor + current].append(factor)
            del found[current]
        else:
            found[current * current].append(current)
            yield current
        current += 1

def fibonacci_generator(upper_limit):
    """Generate the sequence of fibonacci numbers less than upper_limit."""
    memoized = {1: 1, 2: 2}
    def fib(n):
        if n in memoized:
            return memoized[n]
        memoized[n] = fib(n - 1) + fib(n - 2)
        return memoized[n]
    for i in range(1, upper_limit):
        if (current := fib(i)) < upper_limit:
            yield current
        else:
            return