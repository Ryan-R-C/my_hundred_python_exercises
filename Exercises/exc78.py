lista = []
laal = ""
while True:
    lista.append(int(input("Type a number:")))

    laal = str(input("Do you want to continue? [Y/N]:")).strip().upper()[0]
    while laal not in "YN":
        laal = str(input("Do you want to continue? [Y/N]:")).strip().upper()[0]
    if laal == "N":
        break
lista.sort(reverse=True)
print("-=-"*30)
print(f'''You typed {len(lista)} numbers

The values decreasingly: {lista} 
''')
if 5 in lista:
    print("The number 5 is on the list.")
else:
    print("The number 5 is not on the list")
