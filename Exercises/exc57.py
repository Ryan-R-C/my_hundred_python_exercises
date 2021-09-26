from math import factorial
print("Factorial Numbers")
print("1:")
ca = int(input("Type here your number:"))
fa = factorial(ca)
print (fa)
print("2:")
c = int(input("Type here your number:"))
x = c
f = 1
print("{}! = ".format(c), end="")
while x > 0:
    print(x, end="")
    print(' x 'if x >1 else " = ", end = "")
    f *= x
    x -= 1
print(f)