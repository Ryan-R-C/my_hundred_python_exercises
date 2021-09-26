from random import randint
from time import sleep
items = ('Rock', 'Paper', 'Scissor')
cpu = randint(0, 2)
print('''Your options:
[0] Rock
[1] Paper
[2] Scissor''')
player = int(input("Which will you choose?"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!")
sleep(1)
print("-=" * 11)
print("The computer chose {}".format(items[cpu]))
print("You chose {}".format(items[player]))
print("-=" * 11)

if cpu == 0:
    if player == 0:
        print("DRAW!")
    elif player == 1:
        print("YOU WIN!")
    elif player == 2:
        print("YOU LOSE!")
elif cpu == 1:
    if player == 0:
        print("YOU LOSE!")
    elif player == 1:
        print("DRAW!")
    elif player == 2:
        print("YOU WIN!")

elif cpu == 2:
    if player == 0:
        print("YOU WIN!")
    elif player == 1:
        print("YOU LOSE!")
    elif player == 2:
        print("DRAW!")
else:
    print("Invalid move!")