import string

def remove_punctuation(input_string):
    punctuations = set(string.punctuation)
    no_punctuation_string = ""

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is not a punctuation character
        if char not in punctuations:
            no_punctuation_string += char

    return no_punctuation_string

# Example:
input_str = input("Enter a string: ")
result = remove_punctuation(input_str)
print("String without punctuation:", result)
