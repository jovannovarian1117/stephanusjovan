# CSV HOMEWORK DATASET
import csv
import pygal
from matplotlib import pyplot as plt

filename = 'activity.csv'
with open(filename) as fl:
    reader = csv.reader(fl)
    header_row = next(reader)
    interval = []
    avg_int = []
    steps = []
    days = []
    for row in reader:
        step = row[0]
        day = row[1]
        if step == "NA":
            steps.append(0)
            days.append(day)
            interval.append(row[2])
        else:
            steps.append(int(step))
            days.append(row[1])
            interval.append(int(row[2]))

    for i in range(0,2356,5):
        the_index = [j for j,row in enumerate(interval) if row == i]
        values = 0
        for k in range(0,len(the_index)):
            values += steps[the_index[k]]
        values = values/len(set(days))
        avg_int.append(values)

print(avg_int)
print("The maximum number of steps is" + str(int(max(avg_int)))+" in the "+str(avg_int.index(max(avg_int))*5)+'th minutes')
intervals = [i for i in range(0,2356,5)]
plt.plot(intervals,avg_int)
plt.xlabel("Intervals")
plt.ylabel("Average")
plt.show()



