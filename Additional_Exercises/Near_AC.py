
#Create a function that when given two strings of letters, 
# determine whether the second can be made from the first by removing one letter. 
# The remaining letters must stay in the same order.

string1 = input("1:")
string2 = input("2:")
 
ans = False
list1 = list(string1)
list2 = list(string2)
 
for index in range(len(list1)):
letter = list1[index]
del list1[index]
if list1 == list2:
 ans = True
 list1.insert(index, letter)
 
print(ans)