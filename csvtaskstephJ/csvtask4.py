# CSV HOMEWORK DATASET
# Help from Nicholas M
import csv
import pygal
from matplotlib import pyplot as plt

def weeks(weeknumber):
    weeknumber = dt.datetime.strptime(weeknumber, "%Y-%m-%d")
    day = weeknumber.weekday()
    if day < 5:
        return "Weekday"
    else:
        return "Weekend"

def getnumberdays(day, state):
    count = 0
    if state == "Weekdays":
        for i in range(0, len(day)):
            if isweekend(day[i]) == "Weekday":
                count +=1
    elif state == "Weekends":
        for i in range(0, len(day)):
            if isweekend((day[i])) == "Weekend":
                count += 1
    return count



