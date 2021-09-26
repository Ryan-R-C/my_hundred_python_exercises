s = " "
while s != "M" and s != "F":
    s = str(input("Your sex is feminine or masculine? [M/F]:")).strip().upper()[0]
    if s != "M" and  s != "F":
        print("You did not type the required thing")
if s == "M":
    print("So, you're a Man!")
elif s == "F":
    print("So, you're a Woman!")
else:
    print(" ")

