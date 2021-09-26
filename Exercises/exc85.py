from random import randint
games = list()
lista = list()
cont = 0
tot = 1
print("-"*30)
print(f"MEGA SENA's GAME!")
print("-"*30)
q = int(input("How many times do you want I raffle?"))
while tot <= q:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    tot += 1
    lista.sort()
    games.append(lista[:])
    lista.clear()
print("-=-"*3, f"Raffling {q} games","-=-"*3 )
for i, l in enumerate(games):
    print(f"Game {i+1}: {l}")
