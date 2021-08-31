import collections
import typing

#### Check Functions

def is_palindrome(s: str) -> bool:
    """Returns True if s is a palidrome."""
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

#### Sequence Generators
def prime_generator(upper_limit: int, start: int=2) -> typing.Generator[int, None, None]:
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

def fibonacci_generator(upper_limit: int) -> typing.Generator[int, None, None]:
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

def perfect_power_generator(exponent: int, upper_limit: typing.Optional[int]=None) -> typing.Generator[int, None, None]:
    """Generate the sequence of natural numbers raised to exponent."""
    current = 1
    while (result := current ** exponent) < (upper_limit or result + 1):
        current += 1
        yield result
    return None

### Sequence Utilities

def grid_slicer(grid: typing.Sequence[typing.Sequence[typing.Any]], 
                start_x: int, start_y: int, count: int, 
                x: int=0, y: int=0) -> typing.List[typing.Any]:
    """Return a slice of a grid (2-d sequence) in any direction.
    
    Arguments:
      grid:     A 2-d sequence
      start_x:  Initial column position in the grid
      start_y:  Initial row position in the grid
      count:    Desired length of the returned slice
      x:        Integer by which to increment the x position to build the slice.
      y:        Integer by which to increment the y position to build the slice.
    Returns:
      A sequence of elements of the grid up to count in length.  If incrementing according
      to x or y would overflow the grid boundaries, incrementation is stopped and the slice
      is returned as is.
    Raises:
      ValueError:  When count, x, or y are not appropriate values for generating a slice,
                   or when (start_x, start_y) is not a valid position on the grid.
    """
    if count < 1 or all((x == 0, y == 0)):
        raise ValueError(f'Can not slice grid with count {count}, x increment {x}, and y increment {y}.')
    row_max = len(grid) - 1
    col_max = [len(r) - 1 for r in grid]
    if row_max < start_y or col_max[start_y] < start_x or start_x < 0 or start_y < 0:
        raise ValueError(f'Invalid position ({start_x}, {start_y}).')
    result = []
    current_x, current_y = start_x, start_y
    for _ in range(count):
        result.append(grid[current_y][current_x])
        current_x += x
        current_y += y
        if current_y > row_max or current_x > col_max[current_y] or current_x < 0 or current_y < 0:
            break
    return result
    
