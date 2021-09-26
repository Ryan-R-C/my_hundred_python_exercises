from Usefull import numbers
x = float(input("Type a num:"))
print(f"You typed {numbers.coin(x)}")
print(f'''The half of {numbers.coin(x)} is {numbers.half(x, formata=True)}
The double of {numbers.coin(x)} is {numbers.double(x, formata=True)}''')
e = float(input(f"PERCENTAGE TIME! \nPecentage:"))
print(f'''{e}% of {numbers.coin(x)} is {numbers.percentange(x, e, formata=True)}
Adding {e}% of {numbers.coin(x)} is {numbers.pluspercentage(x, e, formata=True)}
Subtracting {e}% of {numbers.coin(x)} is {numbers.minuspercentage(x, e, formata=True)}''')
