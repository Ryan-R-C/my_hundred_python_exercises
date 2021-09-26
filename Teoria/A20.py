def lin():
    print("-=-"*30)
lin()
print("Pinto")
lin()

def letter(msg):
    print("-=-"*30)
    print(msg)
    print("-=-"*30)

letter("Sistem sucks")

def sum(a,b):
    s = a + b
    print('-=-'*15)
    print(f"A = {a}; B = {b}")
    print(f"A + B = {s}")
    print('-=-'*15)
sum(1,2)
#Pode-se mudar a ordem:
sum(b=2, a=1)

def contador(* numb):
    print(numb)
#Mesma coisa que dizer que não sabe quantos numeros vem aí.
contador(7, 1, 9)

#Por exemplo, para dobrar os valores:
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos += 1
        print(lst)
valores = [6, 4, 9]
dobra(valores)
