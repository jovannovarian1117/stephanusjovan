# Question 2:
# with the help of Adriel.
valueList = []
valueMod = {}
count = 0
while count < 10:
    tenNumbers = int(input("input numbers please thank you!!"))
    valueList.append(tenNumbers)
    count += 1
for i in valueList:
    output = i % 42
    valueMod[output] = 0
print (len(valueMod.keys()))







