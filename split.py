
myString = '2.2 1.3 8.8 5.5 3.4 12.5 9.9 2.7 7.1 1.1'
mylist = myString.split()

print("The list below after splitting '2.2 1.3 8.8 5.5 3.4 12.5 9.9 2.7 7.1 1.1")
print(mylist)
print('\n')

mylist.sort()
print("The list below after split and sort '2.2 1.3 8.8 5.5 3.4 12.5 9.9 2.7 7.1 1.1")
print(mylist)
print('\n')

print("smallest number is " + min(mylist))
print("largest number is " + max(mylist))
print(len(mylist))
