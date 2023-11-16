# To calculate 10 terms of Fibonacci series

fibonacci_numbers = [0, 1]  # list of fibonacci no. with two initial values created

while len(fibonacci_numbers) < 10:
      next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]  # Next fibonacci no is created
      fibonacci_numbers.append(next_number)                        # Next term is added to the list

print(fibonacci_numbers) # the entire list of 10 fibonacci no. is printed on the screen
