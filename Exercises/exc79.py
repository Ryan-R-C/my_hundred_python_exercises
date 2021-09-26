lista = []
listodd = []
listeven = []
x = ""
while True:
    n = int(input("Type a number:"))
    if n % 2 == 0:
        listeven.append(n)
    else:
        listodd.append(n)
    lista.append(n)
    x = str(input("Continue? [Y/N]")).strip().upper()[0]
    while x not in "YN":
        x = str(input("You typed something wrong. Continue? [Y/N]")).strip().upper()[0]
    if x == "N":
        break
print(f''' Your complete list is {lista};
The list with just odds is {listodd}
And the list of evens {listeven}''')