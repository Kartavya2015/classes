#empty tuple
empty_tuple = ()
my_tuple = ()

#tuple with integers
my_tuple = (1,2,3,4,5)

#tuple with mixed data types
my_tuple = (1, "jack", 3.5)

#nested tuple
nested_tuple = (1, 2, (3, 4), 5)

#returning a tuple
def return_tuple():
    return (1, 2, 3)

#accessing tuple elements using indexing
my_tuple = ('bath', 'he he he', 'cancled', 'for', 'fun', 'today')
print(my_tuple[1])
print(my_tuple[5])

#Iterating through a tuple
for letter in (my_tuple[1:6]):
    print("hello", letter)
