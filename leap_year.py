userinput = (input("Enter the symbol: "))

if userinput.isdigit:
    print("It is not a letter")
elif userinput.isalpha:
    print(userinput, "is a letter")
else:
    print("invalid")