import math

class date(object):
    def __init__(self, month, day, year):
        self.day = day
        self.month = month
        self.year = year

def smaller_date(date1, date2):
    """Given two dates, returns a tuple representing
    <smaller date>, <larger date>."""
    if (date1.year <= date2.year):
        if (date1.year == date2.year):
            if (date1.month <= date2.month):
                if (date1.month == date2.month):
                    if (date1.day <= date2.day):
                        # dates could be equiv here as well
                        return date1, date2
                    else:
                        return date2, date1
                else:
                    return date1, date2
            else:
                return date2, date1
        else:
            return date1, date2
    else:
        return date2, date1

def month_diff_bw_dates(date1, date2):
    """If two dates are more than a month apart, returns 1.
    Exactly a month apart (based on day value for each date), returns 0.
    Less than a month apart, returns -1."""
    result = 0

    # more than a month
    # years differ too much
    if (math.fabs(date1.year - date2.year) > 1):
        result = 1
    else:
        # detect year boundary scenario
        if (math.fabs(date1.year - date2.year) == 1):
            # requires knowing which date is smaller
            smaller_date = date1 if date1.year < date2.year else date2
            larger_date = date1 if (smaller_date != date1) else date2
        
            # years differ, but we've got the boundary scenario of
            # 12/x and 1/(x+1); 
            if ((smaller_date.month == 12) and (larger_date.month == 1)):
                # more than a month if days are too far apart
                if (larger_date.day > smaller_date.day):
                    result = 1
                else:
                    # exactly a month
                    if (larger_date.day == smaller_date.day):
                        result = 0
                    else:
                        # less than a month
                        result = -1
        else:
            # years are the same
            # difference b/w month values is > 1
            if (math.fabs(date1.month - date2.month) > 1):
                result = 1
            else:
                # years are the same, month 1 apart
                if (math.fabs(date1.month - date2.month) == 1):
                    # requires knowing which date is smaller
                    smaller_date = date1 if date1.month < date2.month else date2
                    larger_date = date1 if (smaller_date != date1) else date2

                    # more than a month if days are too far apart
                    if (larger_date.day > smaller_date.day):
                        result = 1
                    else:
                        # exactly a month
                        if (larger_date.day == smaller_date.day):
                            result = 0
                        else:
                            # less than a month
                            result = -1
                else:
                    result = -1

    return result