a = int(input("enter a value: "))
b = int(input("enter a value2: "))
c = int(input("enter a value3: "))

avg = (a + b + c)/3
print("avg=",avg)
if avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d, %d" %( avg, a, b, c))
if avg > a and avg > b:
    print("%d is higher than %d, %d" %( avg, a, b, ))
if avg > b and avg > c:
    print("%d is higher than %d, %d" %( avg, b, c))
if avg > a and avg > c:
    print("%d is higher than %d, %d" %( avg, a, c))
if avg > a:
    print("%d is higher than %d," %( avg, a))
if avg > b:
    print("%d is higher than %d," %( avg, b))
if avg > c:
    print("%d is higher than %d," %( avg, c))
else:
    print("invalid")