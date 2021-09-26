from Usefull import numbers
x = float(input("Type a num:"))
print(f"You typed {numbers.coin(x)}")
print(f'''The half of {numbers.coin(x)} is {numbers.half(x)}
The double of {numbers.coin(x)} is {numbers.double(x)}''')
e = float(input(f"PERCENTAGE TIME! \nPecentage:"))
print(f'''{e}% of {numbers.coin(x)} is {numbers.percentange(x, e)}
Adding {e}% of {numbers.coin(x)} is {numbers.pluspercentage(x, e)}
Subtracting {e}% of {numbers.coin(x)} is {numbers.minuspercentage(x, e)}''')
