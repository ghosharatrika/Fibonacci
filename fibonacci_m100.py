# From fibonacci_module.py importing the generate_fibonacci function to calculate 100 terms and to find how much time is taken to calculate it

from fibonacci_module import generate_fibonacci
import timeit

start_time = timeit.default_timer()  # To get the time at which the calculation has started
first_100_fibonacci = generate_fibonacci(100)
elapsed_time = timeit.default_timer() - start_time  # To get how much time is taken to perform the task

print("First 100 Fibonacci numbers:", first_100_fibonacci)
print(f"Time taken to generate 100 Fibonacci numbers: {elapsed_time} seconds")
