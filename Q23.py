def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Example:
temp_type = input("Enter temperature type to convert (C for Celsius, F for Fahrenheit): ").upper()
if temp_type == 'C':
    celsius_temp = float(input("Enter temperature in Celsius: "))
    converted_temp = celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp} Celsius is equal to {converted_temp:.2f} Fahrenheit")
elif temp_type == 'F':
    fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
    converted_temp = fahrenheit_to_celsius(fahrenheit_temp)
    print(f"{fahrenheit_temp} Fahrenheit is equal to {converted_temp:.2f} Celsius")
else:
    print("Invalid temperature type entered. Please enter 'C' or 'F'.")
