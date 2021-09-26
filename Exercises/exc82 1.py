num = [[], []]
v = 0
for c in range(1,8):
    v = int(input(f"Type the {c}° number : "))
    if v % 2 == 0:
        num[0].append(v)
    else:
        num[1].append(v)
num[0].sort()
num[1].sort()
print(f"The evens: {num[0]}")
print(f"The odds: {num[1]}")