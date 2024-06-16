def sum_of_digits(number):
    str_number = str(number)
    # To calcualte the sum of digits
    digit_sum = 0
    # Iterate through each digit in the string representation
    for digit in str_number:
        digit_sum += int(digit)
    return digit_sum

# Example:
number= int(input("Enter a number: "))
sum = sum_of_digits(number)
print(f"The sum of digits of {number} is: {sum}")
