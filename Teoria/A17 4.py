a = [2, 3, 4, 7]
b = a
b[2] = 0
# ^ NÃO MEXE APENAS NA B, MAS TBM NA A! CRIA UMA LIGAÇÃO ENTRE ELAS.
print(f"Lista a é {a} e a lista b é {b}")

b = a[:]
b[2] = 999
print(f"Lista a é {a} e a lista b é {b}")
# AGORA SIM ELE RECEBEU APENAS OS VALORES, AGORA SÃO DIFERENTES!