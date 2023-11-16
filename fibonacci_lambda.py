# To calculate fibonacci series using lambda
from functools import reduce

# n is the no. of terms
fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

print(fib(10))
