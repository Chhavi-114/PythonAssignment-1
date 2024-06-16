def convert_to_title_case(input_string):
    # To split the input string into words:
    words = input_string.split()

    # To store capatalised words:
    title_case_words = []

    # Iterate through every word, capitalize the first letter, and then append to the 'title_case_words' list:
    for word in words:
        # To capitalize the first letter and concatenate with the rest of the word
        title_case_word = word[0].upper() + word[1:].lower()
        title_case_words.append(title_case_word)

    # To join the title case words into a single string
    title_case_string = ' '.join(title_case_words)

    return title_case_string

# Example:
input_str = input("Enter a string: ")
title_case_str = convert_to_title_case(input_str)
print("Title Case: ", title_case_str)
