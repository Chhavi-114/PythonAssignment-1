def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example:
number = int(input("Enter a number: "))
F = factorial(number)
print(f"The factorial of {number} is {F}.")

