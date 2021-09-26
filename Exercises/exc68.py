totcash = 0
cont = 50
v = int(input("Type here how much cash you want:"))
num = v
while True:
    if num >= cont:
        num -= cont
        totcash += 1
    else:
        if totcash > 0:
            print(f"{totcash} note(s) of $ {cont}")
        if cont == 50:
            cont = 20
        elif cont == 20:
            cont = 10
        elif cont == 10:
            cont = 1
        totcash = 0
        if num == 0:
            break
