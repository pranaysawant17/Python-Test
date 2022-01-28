'''
#1.Convert numeric words to numbers

word= input("enter number  to convert: ")
num = {"one": 1, "two": 2, "three": 3, "four":4, "five": 5, "six":6, "seven":7, "eight":8, "nine":9, "zero":0}

print(num[word.lower()])




# 2.    Word    location in String:
def word_loc(a,b):
    c=0
    for i in a.split():
        if i == b:
            c+=1
            return c
        else:
            c+=1
            continue
print(word_loc("geeksforgeeks is best for geeks", 'best'))
'''
#3.Right and Left Shift characters in String

word= "geeksforgeeks"

r_s = 7
l_s = 3


mod = (r_s -l_s)% len(word)

print(word[mod:]+word[:mod])


'''
#4.Sort String list by K character frequency

def list_sort(a,b):
    return  sorted(a,key = lambda x:x.count(b), reverse=True)

print(list_sort(['geekforgeekss', 'is', 'bessst', 'for', 'geeks'],'s'))

#5 Program to accept the strings which contains all vowels
word = input("enter your word: ")
lst=[]
for i in word:
    if i.lower() in ['a', 'e', 'i', 'o', 'u']:
        lst.append(True)

    else:
        lst.append(False)
if all(lst)== True:
    print( "Word is accepted")
else:
    print("Not accepted")


'''





