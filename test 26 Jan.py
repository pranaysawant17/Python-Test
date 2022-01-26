
#(1) write a  Python program Accessing nth element from tuples in list.
n = int(input("Enter number you need: "))
t = [(1, 7) , (5 , 8) ,10 ,42]
print("{0}th element is :{1}".format(n, t[n-1]))


#(2) write a python programto find number of days between two given dates.

from datetime import date


def numOfDays(date1, date2):
    a, b ,c= [int(i) for i in date1.split('/')] #for [13, 12, 2018]
    d,e,f= [int(i) for i in date2.split('/')]
    date1 =date(c,b,a) # date( 2018 , 12 , 13 ) format
    date2 = date(f,e,d)
    return (date2 - date1).days

print(numOfDays('13/12/2018', '25/2/2019'))
print(numOfDays('1/1/2004', '1/1/2005'))






#(3) Write Python program to find the sum of all items in a dictionary.
def sum_dict(a):
    sum=0
    for i in a.items():
        sum+=i[0]+i[1]
    print(sum)
sum_dict({1:2,5:6,7:7,8:1})




#(4) write a Python program to check if a string has at least one letter and one number
def str_num(a):
    l=0
    n=0
    for i in a:
        if i.isdigit():
            n+=1
        elif i.isalpha():
            l+=1
    if n>0 and l>0:
        print( True)
    else:
        print(False)
str_num("welcome2ourcountry34")
str_num("stringwithoutnum")

# WAP to find cumsum:
def cumsum(a):
    new =[]
    sum=0
    for i in a:
        sum+=i
        new.append(sum)
    print( new)
    

cumsum([1,10,15,60])
