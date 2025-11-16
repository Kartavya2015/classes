studentdata = {'id1' : {'name':'Alice','age': 10},
              'id2': {'name':'Bob','age': 12},
                'id3': {'name':'Alice','age': 10},
                'id4': {'name': 'Kartavya', 'age': 10}

}
result = {}
for key, value in studentdata.items():
    if value not in result.values():
        result[key] = value
print(result)