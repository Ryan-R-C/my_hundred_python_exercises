def tes (b):
    global a
    b += 3
    c = 2
    print(f'''A dentro vale {a}
B dentro vale {b}
C dentro vale {c}''')

a = 5
tes(a)
print(f"A fora vale {a}")