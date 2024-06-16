def read_multiple_lines():
    lines = []
    while True:
        line = input("Enter a line (press Enter to finish): ")
        if line == "":
            break
        lines.append(line)
    return lines

# Read multiple lines from the input given by the user
input_lines = read_multiple_lines()

# Print all the lines entered by the user
print("\nLines entered:")
for line in input_lines:
    print(line)
