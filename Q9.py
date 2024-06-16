def check_substring(input_string, substring):
    if substring in input_string:
        return True
    else:
        return False

# Example usage:
input_str = "Hi, I am V."
sub_str = "I am V."
if check_substring(input_str, sub_str):
    print(f"Substring '{sub_str}' found in string '{input_str}'")
else:
    print(f"Substring '{sub_str}' not found in string '{input_str}'")

