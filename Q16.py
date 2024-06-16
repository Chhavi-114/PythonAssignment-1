def count_character_frequency(input_string):
    char_frequency = {}

    # Counting the frequency of the each character
    for char in input_string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return char_frequency

# Example:
input_str = input("Enter a string: ")

# Counting the frequency of the characters in the input string
frequency = count_character_frequency(input_str)

# To print the character frequencies
print("\nCharacter frequencies:")
for char, count in frequency.items():
    print(f"Character '{char}' occurs {count} time(s)")
