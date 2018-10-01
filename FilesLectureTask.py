# Question 1
# word count
# unique (happy)
# most common (most occur) <-- top 10

#from collections import Counter
#j = open("text.txt","r")
#chara = j.read().lower()
#line = chara.split()
#count = Counter(line)

#for x in count:
#    if(count.get(x) == 1):
#        print (x)



#hapax()
# Question 2
#article1 = open("text2.txt" ,"r")
#article2 = open("text2_two.txt","w")
#with article1 as f:
#    with article2 as j:
#        for text in f:
#           j.write(text)
# for cf in article2:



# Question 3
#def avg():
#    article = open("text2.txt" , "r")
#    alphabets = article.read()
#    words = alphabets.split()
#    total = 0
#    devision = 0
#    for i in alphabets:
#        total += 1
#    for j in words:
#        devision += 1
#    print (total/devision)
#avg()

# Question 4
textFile = open("text4.txt", 'r')
text = str(textFile.read())
text = (text + " ")
startFrom = 0
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
punc = ['!', '?', '.', ',']
others = ['Mr.', 'Mrs.', 'Jr', 'Dr.']
for j in range(0, len(text) - 1):
    if text[j] == "." and text[j + 1] in numbers:
        continue
    elif text[j - 1] in alphabets and text[j - 2] == ".":
        continue
    elif text[j - 2:j + 1] in others or text[j - 3:j + 1] in others:
        continue
    elif text[j] == "." and text[j + 1] in alphabets:
        continue
    elif text[j] == "." and text[j + 1] in punc:
        continue
    elif text[j] in punc:
        print(text[startFrom:j + 1])
        startFrom = j + 2


