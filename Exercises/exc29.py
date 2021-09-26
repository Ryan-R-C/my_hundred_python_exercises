print("SSUP! Today we'are going to se if you have a triangle!")
a = int(input("Put the an angle."))
b = int(input("Now, please, another one."))
c = int(input("Type the last one."))
if a + b > c or b + c > a or a + c > b :
    print("Yes, it does!")
else:
    print("No sorry.")