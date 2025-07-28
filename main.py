def calculator():
    while True:
        print("\n=== Simple Calculator ===")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulo (%)")
        print("6. Exit")

        choice = input("Choose an operation (1-6): ")

        if choice == '6':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = num1 + num2
                    print(f"Result: {num1} + {num2} = {result}")
                elif choice == '2':
                    result = num1 - num2
                    print(f"Result: {num1} - {num2} = {result}")
                elif choice == '3':
                    result = num1 * num2
                    print(f"Result: {num1} * {num2} = {result}")
                elif choice == '4':
                    if num2 != 0:
                        result = num1 / num2
                        print(f"Result: {num1} / {num2} = {result}")
                    else:
                        print(" Error: Division by zero is not allowed.")
                elif choice == '5':
                    if num2 != 0:
                        result = num1 % num2
                        print(f"Result: {num1} % {num2} = {result}")
                    else:
                        print(" Error: Modulo by zero is not allowed.")
            except ValueError:
                print(" Invalid input. Please enter numbers only.")
        else:
            print(" Invalid choice. Please select from 1 to 6.")

# Run the calculator
calculator()