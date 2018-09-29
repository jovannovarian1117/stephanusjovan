def pascaltriangle(n_rows):
    results = []
    for _ in range(n_rows):
        row = [1]
        if results:
            lastRow = results[-1]
            row.extend([sum(pair) for pair in zip(lastRow, lastRow[1:])])
            row.append(1)
        results.append(row)
    return results
for j in pascaltriangle(7):
   print(j)
# Source
# https://stackoverflow.com/questions/24093387/pascals-triangle-for-python
# bibliography
# User, S. O. (2014, June 7th). StackOverflow Python. Retrieved September 2018,
# from Pascal's triangle for python:
# https://stackoverflow.com/questions/24093387/pascals-triangle-for-python