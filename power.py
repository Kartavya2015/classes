basenumber = int(input("Enter the root number: "))
power = int(input("Enter the power: "))

result = 1   # start with 1

for i in range(power):
    result *= basenumber   # multiply base 'power' times

print(f"{basenumber} powered up to {power} is: {result}")
