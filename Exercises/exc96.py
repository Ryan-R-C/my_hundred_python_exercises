def x(msg):
    t = len(msg) + 4
    print("~"*t)
    print(f"  {msg}")
    print("~"*t)
    print()

def anls(* num):
    print(f"Analyzing...\nThe numbers are: {num}.")
    g = 0
    lista = list()
    lista.append(num)
    t = len(num)
    print(f"There were {t} numbers registered!")
    for c in lista:
        for x in c:
            if c == 1:
                g = x
            else:
                if x >= g:
                    g = x
    print(f"And the greater number was {g}.")
    print("-=-"*20)

x("99th exercise!")

anls(3,5,4)
anls(4,7,0)
anls(1,2)
anls(6)
anls()