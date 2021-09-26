from random import randint
a = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for n in a:
    print(f"{n}", end=" ")
print(f" \nThe greater number of them was {max(a)}")
print(f"The lower number of them was {min(a)}")