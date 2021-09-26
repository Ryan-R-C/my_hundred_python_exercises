n = cont = x = 0
r = ""
while r != "N":
    while cont != 5:
        n = int(input("Type here a number:"))
        x += n
        cont += 1
    r = str(input("Do you want it again?[Y/N]:")).upper
print("End")
