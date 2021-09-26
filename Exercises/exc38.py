print("Hey there! Today's exercise is about triangles, cool huh? \n So let's see if it makes a triangle and if it does which.")
a = int(input("Put the an angle."))
b = int(input("Now, please, another one."))
c = int(input("Type the last one."))
if a + b > c or b + c > a or a + c > b :
    print("Yes, it does!", end="")
    if a == c == b:
        print("So... It's a equilateral triangle. Cool! ")
    elif a != c and a != b and b != c :
        print("It's a scalene triangle!")
    else:
        print("You can form a isosceles triangle")
else:
    print("Sorry you can't form a triangle.")
