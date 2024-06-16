def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)

# Example:
if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    read_file(file_name)
