lista = list()
laal = ""
while True:
    n = int(input("Type a number:"))
    if n not in lista:
        lista.append(n)
        print("Number added")
    else:
        print("You already typed this number. I won't add that one in he list!")
    laal = str(input("You want to add more number in your list? [Y/N]:")).strip().upper()[0]
    while laal not in "YN":
        laal = str(input("Sorry, you typed something worng. You want to add more number in your list? [Y/N]:")).strip().upper()[0]
    if laal == "N":
        break
print("-=-"*30)
lista.sort()
print(f"Your list is {lista}")
