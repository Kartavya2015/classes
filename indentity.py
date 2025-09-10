x = 20

if (type(x)) is int:
    print("True")
else:
    print("False")

x = 5.0

if (type(x)) is not float:
    print("False")
else:
    print("True")

x = 20
y = 20

if (x is y):
    print("X and Y are same identy")

x = 20
y = 67

if (x is not y):
    print("X an Y are diffrent identies")