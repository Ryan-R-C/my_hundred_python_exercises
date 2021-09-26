#Number formatation
#MATH

n = int(input("Type here your number"))
print("Your number is {}".format(n))
print("Your number has {} unit(s).".format(n))

if n > 10:
    print("Has {:.0f} dozen(s).".format(n/10))
    if n> 100:
        print("Your number has {:.0f} hundred(s).".format(n/100))
        if n > 1000:
            print("And {:.0f} thousand(s).".format(n/1000))