# CSV HOMEWORK DATASET
import csv
import pygal
from datetime import datetime
#from matplotlib import pyplot as plt

filename = 'activity.csv'
with open(filename) as fl:
    reader = csv.reader(fl)
    header_row = next(reader)
    current_date = datetime.strptime('2012-10-1','%Y-%m-%d')
    day = []
    steps_per_day = []
    steps_total = 0
    total_days = 0
    total_steps = 0

    for row in reader:
        if current_date == datetime.strptime(row[1],'%Y-%m-%d'):
            try:
                step_number = int(row[0])
            except ValueError:
                continue
            else:
                steps_total += step_number
        else:
            steps_per_day.append(steps_total)
            day.append(current_date)
            steps_total = 0
            current_date = datetime.strptime(row[1],'%Y-%m-%d')
            try:
                step_number = int(row[0])
            except ValueError:
                continue
            else:
                steps_total += step_number
        try:
            total_steps += (int(row[0]))
        except ValueError:
            continue
steps_per_day.append(steps_total)
day.append(current_date)
total_days = len(day)
mean = int(total_steps/total_days)
sort = sorted(steps_per_day)
print(sort)

hist = pygal.Bar()
hist.title = "Total number of steps per day"
hist.x_title = "The days"
hist.y_title = "Step Numbers"
hist.add("Number of steps per day",steps_per_day)
hist.render_to_file("task.svg")

print(total_steps)
print(total_days)
print(int(mean))
print(sort[30])



