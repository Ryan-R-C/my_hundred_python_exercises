contp = A = cheapest = cont = 0
cheapname = " "
while True:
    n = str(input("Type here the product's name:"))
    p = float(input("Here the price:$ "))
    z = str(input("Do you want to continue?[Y/N]")).strip().upper()[0]
    while z not in "YN":
        z = str(input("You typed something wrong. Do you want to continue?[Y/N]")).strip().upper()[0]
    cont += 1
    A += p
    if p > 1000:
        contp += 1
    if cont == 1 or p < cheapest:
        cheapest = p
        cheapname = n
    if z == "N":
        break
print(f'''The total price is {A};
{contp} products are greater than $1000;
{cheapname} is the cheapest product that cost ${cheapest}.''')
