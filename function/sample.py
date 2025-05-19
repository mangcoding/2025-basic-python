from datetime import datetime

def calcAgebyYear(yearOfBirth) :
    currentYear = datetime.now().year
    age = currentYear - yearOfBirth
    return age

year_of_date = int(input("What is your birth year? :"))
age = calcAgebyYear(year_of_date)
print("your age is",age,"years old")