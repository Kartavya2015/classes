# Simple Calculator Program
def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	if b == 0:
		return "Error: Division by zero"
	return a / b

def calculator():
	print("Select operation:")
	print("1. Addition (+)")
	print("2. Subtraction (-)")
	print("3. Multiplication (*)")
	print("4. Division (/)")
	choice = input("Enter choice (1/2/3/4): ").strip()

	if choice not in ("1", "2", "3", "4"):
		print("Invalid choice. Exiting.")
		return

	try:
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
	except ValueError:
		print("Invalid number entered. Exiting.")
		return

	if choice == "1":
		result = num1 + num2
	elif choice == "2":
		result = subtract(num1, num2)
	elif choice == "3":
		result = multiply(num1, num2)
	else:  # choice == "4"
		result = divide(num1, num2)

	print(f"Result: {result}")

if __name__ == "__main__":
	calculator()
	print("Thank you for using the calculator!")
print("i used codingal asstant")
# This is a simple calculator program that performs basic arithmetic operations.
# It supports addition, subtraction, multiplication, and division.
("i added this line to test ")