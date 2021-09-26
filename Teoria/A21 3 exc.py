def factorial(n= 1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f

n = int(input("Type a number: "))
r = factorial(n)
print("It's equals to {}".format(r))