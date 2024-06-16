def find_min_max(numbers):
    if not numbers:
        return None, None  
    
    min_value = min(numbers)
    max_value = max(numbers)
    return min_value, max_value

# Example:
numbers = [1, 5, 2, 9, 1, 7, 30]
min_val, max_val = find_min_max(numbers)
print(f"Minimum value: {min_val}, Maximum value: {max_val}")
