# num = (2, 5, 9, 1)
# num[2] = 3 -> It was impossible, but now witg=h lists it isn't anymore!
num = [2, 5, 9, 1]
print(num)
num[2] = 999
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)

print(f"And this list have {len(num)} elements.")

num.insert(2, 0)
print(num)

num.pop(2)
print(num)

if 5 in num:
    num.remove(5)
    print(f"With the number 5 removed the list's gonna be {num}")
else:
    print("We didn't find the number 5.")