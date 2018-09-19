mult = 1
count = 6
while mult <= count:
    print ("*"*mult)
    mult = mult+1


mult = 1
count = 6
while mult <= count:
    print (" "*(count-mult) + "*"*mult)
    mult = mult+1

mult = 1
count = 8

while mult <= count:
    print (" " * (count - mult)+ "*"*mult+ "*"*(mult-1))
    mult = mult + 1