price = float(input("Type here the whole price."))
print('''Our forms of payment are
[1] In cash or Bank check - 10% of discount.
[2] In cash on the credit card - 5% of discount.
[3] In 2 times on the credit card - Normal price.
[4] In more than 3 times on credit card - + 20%
''')
form = int(input("Type which form you want."))
print("The price is", end="")
if form == 1:
    x1 = price - (price*0.1)
    print(" {}".format(x1))
elif form == 2:
    x2 = price-(price*0.05)
    print(" {}".format(x2))
elif form == 3:
    print(" {}".format(price))
elif form == 4:
    x3 = price+(price*0.25)
    print(" {}".format(x3))
else:
    print(" Sorry, try again.")