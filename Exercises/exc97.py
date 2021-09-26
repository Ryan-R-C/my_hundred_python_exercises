def x(msg):
    t = len(msg) + 4
    print("~"*t)
    print(f"  {msg}")
    print("~"*t)
    print()

def y(q):
    from random import randint
    z = randint(4,6)
    lst = []
    for c in range(1,z):
        lst.append(randint(1,6))
    print(f"It was sorted {z-1} values.\nValues {lst}.")
    cont = 0
    for w in lst:
        if w % 2 == 0:
            cont += w
    print(f"The sum of the odds is {cont}")
y(1)