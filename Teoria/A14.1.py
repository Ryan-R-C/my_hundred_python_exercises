n = 1
par = impar = 0
while n!= 0:
    if n!= 0:
        n = int(input("Type a nunber:"))
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("You typed {} even(s) and {} odd(s) number(s).".format(par, impar))

