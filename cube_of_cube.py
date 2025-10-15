def cube(number):
    return number * number * number #or number ** 3

def cube_of_cube(num):
    if num % 3 == 0:
        return cube_of_cube(num)
    else:
        return False

print(cube(30))
print(cube(9))    