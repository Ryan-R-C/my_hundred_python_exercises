greater = lower = x = y = 0
valores = list()
for cont in range(0,5):
    valores.append(int(input(f"Positon {cont} - Type a value:")))

for c, v in enumerate(valores):
    if c == 0:
        greater = lower = v
    if c > 0:
        if v > greater:
            greater = v
            x = c
        if v < lower:
            lower = v
            y = c
print("The lower value was {} in {} and the greater was {} in {} ".format(lower, y+1, greater, x))
