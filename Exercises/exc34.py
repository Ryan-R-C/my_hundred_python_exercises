print("Let'see which number is bigger")
a = int(input("Type here the first number."))
b = int(input("And here the second, please"))
if a > b:
    print("The number {} is bigger than {}!".format(a, b))
elif b > a:
    print("The number {} is bigger than {}!".format(b, a))
else:
    print("They are the same number!")
