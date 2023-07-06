test_list = [[3, 4, 5], [1, 2, 5], [4, 1, 5]]
 
# printing original lists
print("The original list is : " + str(test_list))
 
res = True
for idx in range(len(test_list[0])):
     
    # getting column
    col = [ele[idx] for ele in test_list]
     
    # checking for all Unique elements
    if len(list(set(col))) != len(col):
        res = False
        print(col)
        break
 
# printing result
print("Are all columns Unique : " + str(res))