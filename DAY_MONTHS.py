def is_leap_year(year):
    """Takes years no. to interpret weather it is leap year or not and return a bool value"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_months(month, year):
    """Takes month no. and year and interpret to return no. of days in that months"""
    if month in (1, 3, 5, 7, 8, 10, 12):
        return "31"
    elif month in (4, 6, 9, 11):
        return "30"
    else:
        if is_leap_year(year):
            return "29"
        return "28"


print("Check no. of days in a month of a specific year :")
months = int(input("Enter the month number : "))
years = int(input("Enter the year : "))
print(f"Number of days in month :{months} and year {years} is {days_in_months(months, years)}")
