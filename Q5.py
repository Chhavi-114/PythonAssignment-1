def write_to_file(file_name, content):
    file = open(file_name, 'w')
    file.write(content)
    file.close()
    print(f"Successfully wrote the content to '{file_name}'.")

# Example:
if __name__ == "__main__":
    file_name = input("Enter the file name to write to: ")
    content = input("Enter the content to write: ")
    write_to_file(file_name, content)
