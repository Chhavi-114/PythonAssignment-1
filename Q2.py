def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

# Example :
number = int(input("Enter a number: "))
result = check_even_odd(number)
print(f"The number {number} is {result}.")
