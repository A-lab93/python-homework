years = int(input("Enter the number of years: "))

month=12
day=365
hour=24
print()

def days():
    return years*day
print(f"number of Days in {years} years:  ", days())
print()

def months():
    return years*month
print(f"number of Months in {years} years:  ", months())
print()

def hours():
    return years*day*hour
print(f"number of Hours in {years} years:  ", hours())
print()