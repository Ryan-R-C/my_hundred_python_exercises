estado = dict()
brasil = list()
for c in range(0,3):
    estado["UF"] = str(input("UF: "))
    estado["sigla"] = str(input("Sigla: "))
    brasil.append(estado.copy())

print(brasil)
for e in brasil:
    for k,v in e.items():
        print(f"O campo {k} tem valor {v}")