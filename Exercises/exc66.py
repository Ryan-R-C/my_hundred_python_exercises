contM = contF20 = Up = 0
while True:
    for F in range(1, 2):
        print("<->"*20)
        S = str(input("Here the sex [M/F/I]:")).strip().upper()[0]
        while S not in "MFI":
            S = str(input("Here the sex [M/F/I]:")).strip().upper()[0]
        A = int(input("And here the age:"))
        if S == "M":
            contM += 1
        if S == "F" and A <= 20:
            contF20 += 1
        if A >= 18:
            Up =+ 1
    x = str(input("Do you want to continue?[Y/N]:")).strip().upper()[0]
    while x not in "YN":
        x = str(input("You typed something wrong. Do you want it again?[Y/N]:")).strip().upper()[0]
    if x == "N":
        break
print(f'''You typed:
A){Up} person(s) who have age greater than 18
B){contM} man(s)
C){contF20} woman(s) who have age lower than 20
''')
