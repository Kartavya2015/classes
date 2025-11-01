try:
        age = int(input("Please enter your age: "))
        if age <= 0:
            pass
        if age % 2== 0:
            print(f"Your age is {age}, which is a even number")
        else:
            print(f"Your age is {age}, which is a odd number")
except ValueError as ex:
    print("Invalid input.\nError details: ", ex)