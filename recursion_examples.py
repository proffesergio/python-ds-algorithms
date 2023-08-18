# Find the factorial of all natural numbers N
# N! = N * (N-1)!

# Exceeding the limit of recursion calls
import sys
sys.setrecursionlimit(20000)
sys.set_int_max_str_digits(50000)

print("Please Enter a number to calculate the factorial: ")
n = int(input())
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print("Factorial of natural number {} is: {}".format(n, factorial(n)))

# Find the sum of all natural number N
# sum(n) = n + sum(n-1)

# print("Please Enter a number to calculate the sum: ")
# n = int(input())

def sum_of(n):
    if n == 0:
        return 0
    partial_output = sum_of(n-1) # recursive function call
    result = partial_output + n
    return result

# print("Sum of the natural number {} is: {}".format(n, sum_of(n)))

# Print all natural number N

# print("Please Enter a number to print all natural number from 1 to n: ")
# n = int(input())
def print_numbers(n):
    if n == 0:
        return 0
    result = print_numbers(n - 1)
    print(n)
    return

# print("Printing all the natural numbers between 1 - N")
# print_numbers(n)

# Print all natural number N
print("Fibonacci Series of n: ")
n = int(input())

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    result = fibonacci(n-1) + fibonacci(n-2)
    return result

# print("Fibonacci Series of {}: {}".format(n, fibonacci(n)))