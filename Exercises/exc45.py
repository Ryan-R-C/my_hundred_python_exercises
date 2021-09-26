print("Sequence starts with 3"
      "3×1=3 or 3×1^2=3 3×4=12 or 3×2^2=12 3×9=27 or 3×3^2=27 ")
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(s + c)
        s += c
        cont = cont + 1
print('And the sum of all {} values are {}'.format(cont, s))
