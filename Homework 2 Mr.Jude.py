# Homework
# Question 1
#def max_of_three(x,y,z):
 #   list = [x,y,z]
  #  print(max(list))
#max_of_three(3,5,1)

# Question 2
#def list(anything):
 #   i = 0
  #  for i in range(len(anything)):
   #     print(len(anything))
#anything = ["a","b","c","d"]
#print(len(anything))

# Question 3
#def vowel(string):
 #   if string == "a" or string == "e" or string == "u" or string == "i" or string == "o":
  #      return True
   # else:
    #    return False
#string = input("input any alphabeth")
#print (vowel(string))

# Question 4
#def reverse(string):
 #  if string == string[::-1]:
  #    return True
   #else:
    #  return False
#string = input("input anything except numbers")
#print (reverse(string))

# Question 5
#def is_member(anything, a):
 #  for i in a:
  #    if i == anything:
   #     break
    #  else:
     #    return False

#anything = input("input anything")
#a = input("input anything")
#print(is_member(anything, a))

# Question 6
#def overlapping():
 #   for a in list1:
  #      for b in list2:
   #            return True
   # else:
    #    return False
#list1 = input("type something please")
#list2 = input("type something please")
#print (overlapping())

# Question 7
#def generate_n_charm(c,expand):
 #   spaces = ""
  #  for x in range (0,c):
   #     spaces += expand
    #print(spaces)

#generate_n_charm(int(input("input numbers please")),str(input("input alphabeths")))

# Question 8
#def histogram(x,y,z):
#    list = [x,y,z]
#    print (x*"*")
#    print (y*"*")
#    print (z*"*")

#x = int(input("x"))
#y = int(input("y"))
#z = int(input("z"))

#print (histogram(x,y,z))

# Question 9
#string = str(input("input any strings please"))
#len_count = []
#count = 0
#while string <= count:
 #   len_count.append()
  #  count += 1
#def list_of_words():
 #   for i in strings:
  #      string.append(len(string))
   # return string

# Question 10
#def find_longest_word(x,y,z):
 #   list = [x,y,z]
  #     return len(x)
  #  elif
#       len(x) >= len(z):
  #      print (len(x))
   # if len(y)>= len(x):
    #    return len(y)
    #elif len(y) >= len(z):
     #   print (len(y))
    #if len(z) >= len(x):
     #   return len(z)
   # elif len(z) >= len(y):
    #    print (len(z))

#x = str(input("input letters"))
#y = str(input("input letters"))
#z = str(input("input letters"))

#print (find_longest_word(x,y,z))

# Question 11
eg_phrase = "the quick brown fox jumps over the lazy dog"

#def is_pangram(phrase):
#    c = 0
#    alphabet = "abcdefghijklmnopqrstuvwxyz"
#    letters_list = ""
#    for char in phrase:
#        for letter in alphabet:
#            if char == letter and char not in letters_list:
#                letters_list += char
#    for char in letters_list:
#        for letter in alphabet:
#            if char == letter:
#                c += 1
#    if c == 26:
#        return True
#    else:
#      print (letters_list, alphabet)
#       return False
#print (eg_phrase)
#print (is_pangram(eg_phrase))

# Question 12
#def make_ing_form(verb):
#    if verb[len(verb)-2:len(verb)+1] == "ie":
#        verb = verb[:-2]
#        verb = verb+"ying"
#        print(verb)
#    elif verb[-1] == "e":
#        verb = verb[:-1]
#        verb = verb+"ing"
#        print(verb)
#    elif (verb[-1] in consonance) and (verb[-2] in vowel) and (verb[-3] in consonance):
#        verb = verb + verb[-1] + "ing"
#        print(verb)
#    else:
#        verb = verb+"ing"
#        print(verb)





