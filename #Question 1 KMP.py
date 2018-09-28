# Assignment 2 TA
# Question 1
#-------------------------------#
list = []
def fullName(name):
    for i in range(0,len(name)):
        if name[i].isupper():
         list.append(name[i].upper())
    print ("".join(list))

fullName(str(input("input name please")))

