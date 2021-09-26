print("Prime number!!!")
tot = 0
num = int(input("Type a number"))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;31m', end=" ")
        tot += 1
    else:
        print('\033[;1m', end=" ")
    print('{} '.format(c), end=" ")
print(" \n \033[0;0m This number was divided {} time(s)".format(tot))
if tot == 2:
    print("That's why it's a Prime number!")
else:
    print("That's why it's not a Prime number!")