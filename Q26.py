def check_prefix_suffix(input_string, prefix, suffix):
    starts_with_prefix = input_string.startswith(prefix)
    ends_with_suffix = input_string.endswith(suffix)
    return starts_with_prefix, ends_with_suffix

# Examplee:
input_str = "Hello, Welcome!"
prefix_to_check = "Hello"
suffix_to_check = "Welcome!"
starts_with, ends_with = check_prefix_suffix(input_str, prefix_to_check, suffix_to_check)
print(f"Starts with '{prefix_to_check}': {starts_with}")
print(f"Ends with '{suffix_to_check}': {ends_with}")
