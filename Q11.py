def generate_fibonacci(n):
    fibonacci_series = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series

# Example:
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_numbers = generate_fibonacci(n)
print(f"The first {n} numbers in Fibonacci series are: {fibonacci_numbers}")
