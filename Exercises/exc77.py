lista = []
n = greater = lower = 0
for c in range(0, 5):
    n = int(input("Type a number"))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print("Added on the last position of the list.")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"Added on the position {pos} of the list.")
                break
            pos +=1
print("-=-"*30)
print(f"The values typed were {lista}")