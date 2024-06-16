def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operator"

# Example:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operators = input("Enter operator (+, -, *, /): ")
result = calculator(num1, num2, operators)
print(f"Result: {result}")
