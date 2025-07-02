#empty dictionary
my_dict = {}

#dictionary with interger keys
my_dict = {1: 'apple', 2: 'banana', 3: 'cherry'}

#dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

my_dict = {'name': "jack", 'age':26}

#output
print(my_dict['name'])
print(my_dict['age'])

#update value
my_dict['age'] = 27
print(my_dict)

#add item
my_dict['address'] = 'Downtown'
print

#remove paticular item
my_dict.pop('age')
print(my_dict)

#accsessing keys
print("Adress:", my_dict.get('address'))

#remove all elements
my_dict.clear()
print(my_dict)