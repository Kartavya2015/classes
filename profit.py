actual_price = float(input("Enter the actual price: "))
sales_price = float(input("Enter the selling price: "))

if (sales_price > actual_price):
    amount = sales_price - actual_price
    print("Total profit is ={0}".format(amount))
else:
    print("No profit")