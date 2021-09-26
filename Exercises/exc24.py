#LIBRARY IMPORT + MATH

from random import randint
print("Try to guess which number,That computer have chosen, between 0 and 5")
aaa = int(input("Which is it?"))
f = randint(0, 5)
if aaa == f :
    print("You got it!")
else:
    print("Sorry. I chose {}! Try again.".format(f))