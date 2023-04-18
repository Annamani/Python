price = 1000000
good_credit = False
if good_credit:
    down_payment=price/10
    print("Down payment should be 10% "+format(down_payment))
else:
    down_payment = price / 20
    print("Down payment should be 20% " + format(down_payment))
print("Down Payment: " +format(down_payment))

