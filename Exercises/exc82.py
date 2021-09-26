lista = list()
temp = list()
for i in range(0,8):
    temp.append(int(input(f"Type here the {i+1}° value:")))
    lista.append(temp[:])
    temp.clear()
    lista.sort()
print(lista)
print("The evens are:")
for n in lista:
    if n % 2 == 0:
        print(f"{n}", end="")
print("\nAnd the odds are:")
for j in lista:
    if j % 2 != 0:
        print(f"{n}", end="")