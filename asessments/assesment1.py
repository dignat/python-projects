#reverse string
str = 'hello'
reverse = str[::-1]
print(reverse)
#build list
list = [0]*3
print(list)
#sort list
list1 = [5,3,4,1]
sorted(list1)
print(list1)
list2 = [(1,2),(3,4)]
#tuples unpacking
for (a, b) in list2:
    print(b)
    
list3 = [(1,2,3), (4,5,6)]
for a,b,c in list3:
    print(b)
 #dictionary   
d = {'k1': 1, 'k2': 2, 'k3': 3}

for key, value in d.items(): #d.vslues() to print only values
    print(value)

x = [1,2,3,4]

for item in x:
    pass
for num in range(0, 11, 2):
    print(num)
    
list4 = [*range(0, 11, 2)] # use generator to create a list
print(list4)
word = 'abcde'

for item in enumerate(word):
    print(item)

from random import shuffle

mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist) # operates in place meaning if i assign to a var it will not shuffle
print(mylist)
#cast user input with float() or int()