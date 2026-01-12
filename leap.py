def leap_year(year):
    # если делится на 4 без остатка
    if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
        return True
    else:
        return False
if __name__ == '__main__':
    leap = leap_year(1900) # False
    # leap = leap_year(1800) # False
    # leap = leap_year(2100)
    print(leap)