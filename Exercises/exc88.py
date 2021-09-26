from random import randint
from time import sleep
from operator import itemgetter
game = {"Player1": randint(1, 6), "Player2":randint(1, 6), "Player3": randint(1, 6), "Player4": randint(1, 6)}
ranking = list()
print(game)
print("-=-"*30)
print("Sorted values:")
for k,v in game.items():
    print(f"The {k} has {v}.")
    sleep(0.5)
ranking = sorted(game.items(), key=itemgetter(1), reverse= True)
print("-=-"*30)
print(ranking)
print("-=-"*30)
for i, v in enumerate(ranking):
    print(f"{i+1}° ranking: {v[0]} with {v[1]} point(s)")
    sleep(0.5)