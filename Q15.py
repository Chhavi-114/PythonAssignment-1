import csv

def read_csv_file(file_name):
    try:
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(', '.join(row))
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except IOError as E:
        print(f"Error: Could not read file '{file_name}'.")
        print(f"Details: {E}")

# Example:
if __name__ == "__main__":
    file_name = input("Enter the CSV file name: ")
    read_csv_file(file_name)
