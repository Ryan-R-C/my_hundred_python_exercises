print('Choose a number')
a = int(input("Type here the first."))
b = int(input("\033[7;Another one please."))
print("Your number is \033[0;37m{}\033[m and \033[0;30m{}\033[m".format(a, b))
