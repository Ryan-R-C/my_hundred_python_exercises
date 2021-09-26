print("Now let's see which is the biggest and the smallest! ")
a = int(input("Enter here a number."))
b = int(input("Enter here an another number."))
c = int(input("Enter here the last one, please."))
smallest = a
biggest = a
if b < a and b < c:
    smallest = b
if c < a and c < b:
    smallest = c
print("The smallest is {}".format(smallest))
if b > a and b > c:
    biggest = b
if c > a and c > b:
    biggest = c
    print("And the biggest is {}".format(biggest))