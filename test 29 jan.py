
#1.	Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
print([i for i in range(1500,2701) if i%35 ==0])

#2.	Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same.
#Sample List : ['abc', 'xyz', 'aba', '1221']

def c_s(a):
    c=0
    for i in a:
      if len(i) >= 2 and i[0] == i[-1]:
       c+=1
    return c

print(c_s(['abc', 'xyz', 'aba', '1221']))

#3.	Write a Python program to find the second largest number in a list.

def sec_large (a):
    return list(sorted(set(a)))[-2]

print(sec_large([1,8,5,9,6,9]))


#4.	Write a Python script to concatenate following dictionaries to create a new one:
def dict_cont(*a):
    new={}
    for i in a:
        for j in i:
          new[j]= i[j]
    return  new
print(dict_cont({1:10, 2:20} ,{3:30, 4:40} ))



#5.	Write a Python program to convert list to list of dictionaries.:
a=["Black", "Red", "Maroon", "Yellow"]
b=["#000000", "#FF0000", "#800000", "#FFFF00"]

print([{'color_name':i,'color_code':j} for i ,j in zip(a,b)])


