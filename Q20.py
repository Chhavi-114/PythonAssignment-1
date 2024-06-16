def calculate_sum(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum

# To enter the list of numbers
num_list = list(map(float, input("Enter numbers separated by space: ").split()))

# To calculate the sum of numbers in the list
result = calculate_sum(num_list)

# To print the sum
print(f"The sum of the numbers is: {result}")


