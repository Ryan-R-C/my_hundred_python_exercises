from time import sleep
a = int(input("Type here the fist number:"))
b = int(input("Type here the second number:"))
x = 0
while x != 5:
    print('''What do you want?
    [1] Add up 
    [2] Multiply
    [3] Which is bigger
    [4] New numbers
    [5] Exit
    So: ''')
    x = int(input('Your option:'))
    if x == 1:
        print(a + b)
    elif x == 2:
        print(a * b)
    elif x == 3:
        if a > b:
            print("{} > {}".format(a,b) )
        elif b > a:
            print("{} > {}".format(b,a))
        else:
            print("{} = {}".format(a, b))
    elif x == 4:
        a = int(input("Type here the fist number,again:"))
        b = int(input("Type here the second number, again:"))
    else:
        print("You did not any of our options. Try again.")
    sleep(2)
print("The End \n check back often")