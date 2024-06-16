from datetime import date

def calculate_age(birth_date):
    today_date = date.today()
    age = today_date.year - birth_date.year - ((today_date.month, today_date.day) < (birth_date.month, birth_date.day))
    return age

def get_birth_date():
    while True:
        try:
            year = int(input("Enter the year of your birth (YYYY): "))
            month = int(input("Enter the month of your birth (MM): "))
            day = int(input("Enter the day of your birth (DD): "))
            birth_date = date(year, month, day)
            return birth_date
        except ValueError:
            print("Invalid date format. Please enter again.")

# To get the birth date from the user
birth_date = get_birth_date()

# To calculate the age of the user
age = calculate_age(birth_date)

# Print age
print(f"You are {age} years old.")
