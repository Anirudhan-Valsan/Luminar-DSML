
def days_between(date1, date2):

    d1, m1, y1 = date1
    d2, m2, y2 = date2


    days1 = y1 * 365 + m1 * 30 + d1
    days2 = y2 * 365 + m2 * 30 + d2

    return abs(days2 - days1)


def add_days(date, days_to_add):

    day, month, year = date
    day += days_to_add

    while day > 30:
        day -= 30
        month += 1
        if month > 12:
            month = 1
            year += 1

    return day, month, year