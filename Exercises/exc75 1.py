listn = list()
greater = lower = 0
for c in range(0,5):
    listn.append(int(input(f"Type the value in the position {c}:")))
    if c == 0:
        greater = lower = listn[c]
    else:
        if listn[c] > greater:
            greater = listn[c]
        if listn[c] < lower:
            lower = listn[c]
print("-=-"*30)
print(f"You typed the values {listn}.")
print(f"The greater number typed was {greater} in the positions ",end=" ")
for i, v in enumerate(listn):
    if v == greater:
        print(f"{i}...",end="")
print()
print(f"\nThe lower number typed was {lower} in the position")
for i, v in enumerate(listn):
    if v == lower:
        print(f"{i}...",end="")
print("")