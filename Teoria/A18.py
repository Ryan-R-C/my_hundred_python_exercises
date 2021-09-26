teste = list()
teste.append("Gustavo")
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])
print(galera)
print("-"*30)
jooj = [["João",19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
print(jooj)
print(jooj[2][1])
for p in jooj:
    print(f"{p[0]} is {p[1]} years old.")