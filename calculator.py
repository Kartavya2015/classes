
def substract(P, Q):
#This function substracts two numbers
    return P - Q

def add(P, Q):
#This function adds two numbers
    return P + Q

def multiply(P, Q):
#This function multiplies two numbers
    return P * Q

def divide(P, Q):
#This function divides two numbers
    return P / Q

#Now we will take the input
print("Select operation.")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

choice = int(input("Enter choice(1/2/3/4): "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == 2:
    print(num1, "-", num2, "=", substract(num1, num2))

elif choice == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == 4:
    print(num1, "/", num2, "=", divide(num1, num2))