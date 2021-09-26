num = list()
odds = list()
evens = list()
while True:
    num.append(int(input("Type a number")))
    x = str(input("Continue? [Y/N]")).strip().upper()[0]
    while x not in "YN":
        x = str(input("You typed something wrong. Continue? [Y/N]")).strip().upper()[0]
    if x == "N":
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        evens.append(v)
    else:
        odds.append(v)
print("-=-"*33)
print(f"""List:{num}
Odds:{odds}
Evens:{evens}""")