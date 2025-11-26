numbers1 = [1,2,3,4,5,6]
numbers2 = [7,8,9,10,11,12]

mapped = map(lambda x,y: x + y, numbers1, numbers2)
print(list(mapped))
#using only map
numbers1 = [1,2,3,4,5,6]
def sq(x):
    return x * x
squared = map(sq, numbers1)
print(list(squared))