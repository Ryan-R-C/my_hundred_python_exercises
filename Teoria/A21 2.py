def somar(a=0,b=0,c=0):
    s = a+b+c
    return s
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False



r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = (6)

print(f"The results of the sums are {r1}, {r2} and {r3}.")

num = int(input("Type a num: "))
if par(num):
    print("It's even!")
else:
    print("It's odd!")