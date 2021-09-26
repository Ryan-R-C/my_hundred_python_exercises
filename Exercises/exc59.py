print("A.P.!")
f = int(input("Your fist term:"))
r = int(input("The reason:"))
x = 1
plus = 9
tot = 0
print("{}".format(f), end=" ")
while plus != 0:
    tot += plus
    while x <= tot:
        f += r
        print("{}".format(f), end=" ")
        x += 1
    print("Pause!")
    plus = int(input("Type here how many terms you want(Type 0 to Finish):"))
print("A.P. finished, {} terms showed.".format(x))