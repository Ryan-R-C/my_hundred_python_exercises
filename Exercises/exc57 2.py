print("Factorial Numbers")
n = int(input("Your number:"))
x = 0
f = 1
print("{}! = ".format(n), end="")
for x in range(1, n):
    f *= n
    n -= 1
print( f )