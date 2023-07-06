#1st task
str = 'Print only the words that start with s in this sentence'
for word in str.split():
    if word[0].lower() == 's':
        print(word)
        
# 2nd task
for num in range(0, 11):
    if num % 2 == 0:
        print(num)
for num in range(0, 11):
    print(num)
        
mylist = [x for x in range(1,51) if x % 3 ==0]
print(mylist)

st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word) % 2 == 0:
        print(word, "even!")
        
#fizzbuzz program

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz', num)
    elif num % 3 == 0:
        print("Fizz", num)
    elif num % 5 == 0:
        print('Buzz', num)
    else:
        print(num)
        
        
str1 = 'Create a list of the first letters of every word in this string'
list = []

for word in str1.split():
    list.append(word[0])
    
print(list)

newlist = [word[0] for word in str1.split()]

print(newlist)