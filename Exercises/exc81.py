l = ""
lista = list()
listaa = list()
greater = lower = 0
while True:
    listaa.append(str(input("Type the person's name:")))
    listaa.append(float(input("And here the person's weight:")))
    if len(lista) == 0:
        greater = lower = listaa[1]
    else:
        if listaa[1] > greater:
            greater = listaa[1]
        if listaa[1] < lower:
            greater = listaa[1]
    l = str(input("Do you wanna continue?[Y/N]: ")).strip().upper()[0]
    lista.append(listaa[:])
    listaa.clear()
    while l not in "YN":
        l = str(input("Do you wanna continue?[Y/N]: ")).strip().upper()[0]
    if l == "N":
        break
print("-=-"*30)
print(f''' Your data is {lista} 
You registered {len(lista)} people
The greater weight is {greater} that belongs to ''', end="")
for p in lista:
    if p[1] == greater:
        print(f'[{p[0]}]')
print(f".\nAnd the lower weight {lower} that belongs to: ",end="")
for p in lista:
    if p[1] == lower:
        print(f"[{p[0]}]", end="")
print(".")