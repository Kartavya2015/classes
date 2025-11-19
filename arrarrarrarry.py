import array
arrary = array.array('i', [1, 2, 3, 4, 3, 3, 3, 5])
print("Original array:", arrary)

print("Number of occurrences of 3 in the array:"+str( arrary.count(3)))

arrary.reverse()
print("Reversed array:")
print(str(arrary))