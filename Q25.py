def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            content = src.read()
            dest.write(content)
        print(f"Successfully copied content from '{source_file}' to '{destination_file}'.")
    except FileNotFoundError:
        print(f"Error: One of the files ('{source_file}' or '{destination_file}') was not found.")
    except IOError as e:
        print(f"Error: Could not read or write files. Details: {e}")

# Example:

    source_file = input("Enter the source file name: ")
    destination_file = input("Enter the destination file name: ")
    copy_file(source_file, destination_file)
