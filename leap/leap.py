def leap_year(year):
    is_leap = False
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            is_leap = True
        elif year % 100 == 0:
            is_leap = False
        else:
            is_leap = True
    return is_leap
