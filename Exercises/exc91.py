l = list()
data = dict()
a = ""
x = 0
while True:
    data["Name"] = str(input("Name: "))
    data["Sex"] = str(input("Sex: ")).strip().upper()[0]
    while data["Sex"] not in "MF":
        data["Sex"] = str(input("You typed something wrong\nSex: ")).strip().upper()[0]
    data["Age"] = int(input("Age: "))
    x += data["Age"]
    l.append(data.copy())
    a = str(input("Do you want to continue?: ")).strip().upper()[0]
    while a not in "YN":
        a = str(input("You typed something wrong. Do you want to continue?: ")).strip().upper()[0]
    if a == "N":
        break
print(f"There were {len(l)} people registered.\n")
Y = x / len(l)
print(f"\nAverage age: {Y:5.2f}\n ")
print("Women registered were:",end="")
for n in l:
    if n["Sex"] == "F":
        print('{n["Name"]};',end="")
print()
print("The people older than the average age are:")
for n in l:
    if n["Age"] > Y:
        for k, v in n.items():
            print(f"{k} = {v};")
    print()
print("The End...")
