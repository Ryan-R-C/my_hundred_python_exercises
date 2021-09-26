pessoas = {"nome": "Gustavo", "sexo":"M", "idade": 22 }
print(pessoas["nome"])
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")
pessoas["nome"] = "Leandro"
pessoas["peso"] = 100
for k, v in pessoas.items():
    print(f"O {k} é {v}.")