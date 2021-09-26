galera = list()
dado = list()
totma = totme = 0
for c in range(0,3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade!")
        totma += 1
    else:
        print(f"{p[1]} é menor de idade!")
        totme +=1
print(f"Você digitou {totma} pessoas que são m aiores de idade e {totme} que são menores de idade.")