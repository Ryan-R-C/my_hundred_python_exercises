n = x = cont = 0
print("The computer will stop when you enter 999.")
n = int(input("Type here a number"))
while n != 999:
    cont += 1
    x += n
    n = int(input("Type here a number"))
print("You typed {} numbers. The sum of all that number is {}.".format(cont, x))
