# Take a full 3-digit number
num = input("Enter a 3-digit number: ")

# Extract digits
a = int(num[0])   # first
b = int(num[1])   # middle
c = int(num[2])   # last

print(f"Before swapping: {a}, {b}, {c}")

# Take input which number to swap with middle (1 or 3)
choice = int(input("Enter position to swap with middle (1 for first, 3 for last): "))

if choice == 1:
    a, b = b, a
elif choice == 3:
    c, b = b, c
else:
    print("Invalid choice! Please enter 1 or 3.")

print(f"After swapping: {a}, {b}, {c}")

# Join back into a number
new_num = int(f"{a}{b}{c}")
print("New number:", new_num)

