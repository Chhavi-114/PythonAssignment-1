def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

# Example:
numbers = [1, 2, 3, 4, 2, 2, 5]
element_to_count = 2
occurrences = count_occurrences(numbers, element_to_count)
print(f"The element {element_to_count} appears {occurrences} times in the list.")
