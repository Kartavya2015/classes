def calc_tipForWaiter(bill_amount, tip_perc):
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total,2)
    print(f"Total amount to be paid: {total} rupees.")

calc_tipForWaiter(1500.34, 45)