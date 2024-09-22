def is_leap_year(Y):
    if Y % 100 == 0:
        return Y % 400 == 0  # Century year: must be divisible by 400 to be a leap year
    else:
        return Y % 4 == 0  # Non-century year: must be divisible by 4 to be a leap year

# Test cases
print(is_leap_year(1600))  # True
print(is_leap_year(1700))  # False
print(is_leap_year(2000))  # True
print(is_leap_year(2020))  # True
print(is_leap_year(2021))  # False
