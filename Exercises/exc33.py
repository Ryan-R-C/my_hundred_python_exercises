num = int(input("Type a number"))
print('''Choose a convertion's base
[1] covert to binary
[2] convert to octal
[3] covert to hexadecimal''')
option = int(input("The chose was:"))
if option == 1:
    print("Your number, {}, converted to binary is {}".format(num, bin(num)[2:]))
elif option == 2:
    print("Your number, {}, converted to octal is {}".format(num, oct(num)[2:]))
elif option == 3:
    print("Your number, {}, converted to Hexadecimal is {}".format(num, hex(num)[2:]))
else:
    print("You typed a wrong number.")