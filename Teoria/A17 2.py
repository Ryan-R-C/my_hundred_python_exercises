#values = list("bla", "blaa", "blaaaa")
# both are the same thing!
#values = ["bla", "blaa", "blaaaa"]
v = []
v.append(5)
v.append(9)
v.append(4)
print(v)
for w in v:
    print(f"{w}...", end="")
for w, c in enumerate(v):
    print(f"\nIn the position {w} I found the value {c}")