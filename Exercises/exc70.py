brasileirão = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print("-="*15)
print(f"The list of 'Brasileirão' is: {brasileirão}")
print("-=" *15)
print(f"The fist five ones are: {brasileirão[:5]}")
print("-=" *15)
print(f"The last four ones are: {brasileirão[-4:]}")
print("-=" *15)
print(f"The teams in alphabetic order: {sorted(brasileirão)}")
print("-=" *15)
print(f'Chapecoense is in {brasileirão.index("Chapecoense")+1}° position')
