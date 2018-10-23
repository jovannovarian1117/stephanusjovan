# CSV HOMEWORK DATASET
# Help from Rino
import csv
import pygal
from datetime import datetime

filename = 'activity.csv'
with open(filename) as fl:
    reader = csv.reader(fl)
    header_row = next(reader)
    fl.seek(0)
    next(fl)
    steps_today = 0
    total_days = 1
    total_steps_nomiss = 0
    current_day = 1
    current_date_formatted = datetime.strptime("2012-10-01", "%Y-%m-%d")
    interval_average = {}

    interval_nomiss_weekend = {}
    interval_nomiss_weekday = {}
    dates_nomiss, steps_nomiss = [], []
    for row in reader:
        if datetime.strptime(row[1], "%Y-%m-%d") == current_date_formatted:
            if row[0] != "NA":
                steps_today += int(row[0])
            else:
                steps_today += interval_average[row[2]]

        else:
            total_days += 1
            dates_nomiss.append(current_date_formatted)
            steps_nomiss.append(steps_today)
            if row[0] != "NA":
                steps_today = int(row[0])
            else:
                steps_today = interval_average[row[2]]
        current_date_formatted = datetime.strptime(row[1], "%Y-%m-%d")

        try:
            total_steps_nomiss += int(row[0])
        except ValueError:
            total_steps_nomiss += interval_average[row[2]]

hist = pygal.Bar()
hist.title = "Total number of steps taken per day. "
hist.x_title = "Days"
hist._y_title = "Number of steps"

hist.add('Number of steps per day', steps_nomiss)
hist.render_to_file('total_number_of_steps_per_day_nomiss.svg')



