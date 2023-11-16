# Generalizing the code to calculate fibonacci series upto n terms


fibonacci_numbers = [0, 1]  # initializing the fibonacci list with first two terms


def generate_fibonacci(n):  # n is the no. of terms upto which the series will be calculated
    if n <= 0:
        print("Incorrect input")
    else:
        while len(fibonacci_numbers) < n:
            next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]  # Calculation of next term of the series
            fibonacci_numbers.append(next_number)                        # Adding the next term to the list
    return fibonacci_numbers
