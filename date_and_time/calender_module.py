# Q. You are given a date. Your task is to find what the day is on that date.
    # Input Format
    # A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.
    
import calendar 

month, day, year = map(int, input().split())

week_day = calendar.weekday(year, month, day)

print(calendar.day_name[week_day].upper())



# Another way with datetime module

import datetime

m, d, y = list(map(int, input().split(' ')))

day = datetime.datetime(y, m, d)

print((day.strftime('%A')).upper())