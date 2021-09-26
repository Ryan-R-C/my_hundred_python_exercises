print("A.P.!")
f = int(input("Your fist term:"))
r = int(input("The reason:"))
x = 0
print("{}".format(f), end=" ")
while x != 9:
    f += r
    print("{}".format(f), end=" ")
    x += 1
print("End")