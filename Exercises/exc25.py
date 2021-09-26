#MATH
n = float(input("Which speed were you? In Km/h."))
f = 7*(n-80)
if n > 80:
    print("Sorry but I need fine you!\n Your traffic ticket is {}".format(f))
else:
    print("Sorry to bother you. You were on the limit")

