'''
#1.Python program to find uncommon words from two Strings

A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

un=[]
for i in A.split(' '):
    if i in B.split(' '):
        continue
    else:
        un.append(i)
for j in B.split(' '):
    if j in A.split(' '):
        continue
    else:
        un.append(j)
print(un)

print(set(B.split(' ')).difference(set(A.split(' '))))
'''

#2.Python program to Replace all Characters of a List Except the given character
test_list =['G', 'F', 'G', 'I', 'S', 'B', 'E','S','T']
replacechr = '*'
remainchr = 'G'

new=[]
for i in test_list:
    if i == remainchr:
        new.append(i)
    else:
        new.append(replacechr)
print(new)


#3. Write a Python program to remove an empty tuple(s) from a list of tuples.
A= [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

lst=[]
for i in A:
    if len(i) == 0:
        continue
    else:
        lst.append(i)
print(lst)

#4 Python program to find common elements in three lists using sets
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

print (list(set(ar1).intersection(set(ar2)).intersection(set(ar3))))


#5.Python – Convert Lists of List to Dictionary

INPUT =[['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]

#OUTPUT = {(‘c’, ‘d’): (3, 4), (‘e’, ‘f’): (5, 6), (‘a’, ‘b’): (1, 2)}

dict1 = {}
for i in INPUT:
    dict1[tuple(i[:2])]= tuple(i[2:])
print(dict1)
