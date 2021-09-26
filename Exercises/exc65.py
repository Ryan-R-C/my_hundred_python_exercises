from random import randint
cont = 0
while True:
    print("Odds or Evens!")
    x = str(input("Odds or Evens, which one will you choose? [O/E]:")).strip().upper()[0]
    while x != "O" and x != "E":
        x = str(input("Sorry you typed something wrong. Odds or Evens, which one will you choose? [O/E]:")).strip().upper()[0]
    num = int(input("Your number:"))
    y = randint(1, 11)
    L = num+y
    print(f"The computer chose {y}, you chose {num}.")
    if x == "O":
        if L % 2 == 0:
            print("You got this! +1")
            cont += 1
        else:
            print("YOU LOOSE!")
            break
    if x == "E":
        if L % 2 != 0:
            print("You got this! +1")
            cont += 1
        else:
            print("YOU LOOSE!")
            break
print(f"Your final score is {cont}")
