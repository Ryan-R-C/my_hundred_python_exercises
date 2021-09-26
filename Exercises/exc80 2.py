exp = str(input("Type a mathematical expression: with() "))
x = []
for simb in exp:
    if simb == "(":
        x.append("(")
    elif simb == ")":
        if len(pilha) > 0:
            x.pop()
        else:
            x.append(")")
            break
if len(x) == 0:
    print("Valid")
else:
    print("Invalid")