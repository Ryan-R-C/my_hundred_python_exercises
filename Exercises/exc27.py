#
n = int(input("Enter here the distance that You will travel. If it be bigger than 200Km We will make a discount"))
if n > 200:
    nc = n*45
    print("It will cost {:.2f}. With the discount, sure.".format(nc))
else:
    wn = n*50
    print("Without the discount it will cost {:.2f}".format(wn))
