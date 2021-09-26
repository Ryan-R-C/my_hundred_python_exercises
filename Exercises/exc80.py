exp = str(input("Type a mathematical expression: "))
x = []
cont9 = cont0 = 0
for simb in exp:
    if simb == "(":
        cont9 += 1
    elif simb == ")":
        cont0 += 1
if cont9 - cont0 == 0:
    print("Valid!")
else:
    print("Invalid!")
