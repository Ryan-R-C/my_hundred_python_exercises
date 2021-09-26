from random import randint
cont = 0
r = randint(0, 10)
print("Try to guess a number between 0 and 10")
win = False
while not win:
    s = int(input("You wanna try?"))
    cont += 1
    if s == r:
        win = True
    else:
        print("You lose!")
        if s < r:
            print("Greater.... Try again.")
        if s > r:
            print("Lesser... Try again.")
print("You Win! {} try(s)".format(cont))


