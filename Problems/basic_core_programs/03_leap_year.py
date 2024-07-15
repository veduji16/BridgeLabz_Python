def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
    return False

year = int(input("Enter a 4-digit year: "))
if len(str(year)) != 4:
    print("Please enter a valid 4-digit year.")
else:
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
