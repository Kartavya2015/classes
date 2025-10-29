try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError as ex:
    print("Exception:", ex)