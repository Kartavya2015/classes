my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(my_set)

#set of mixed data types
my_set = {1, "Hello", 3.14, (1, 2), True}
print(my_set)

#set cannot have duplicate
my_set = {1, 2, 2, 3, 4, 5, 5, 5}
print(my_set)

#we can create a list using a list
my_set = set([1, 2, 3, 4, 5])
print(my_set)

#remove a number from a set
numset = ([1, 2, 3, 4, 5])
print("original set:", numset)
numset.pop()
print("after pop:", numset)