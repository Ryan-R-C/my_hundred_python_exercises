from Usefull import numbers
x = float(input("Type a num:"))
print(f'''The half of {x} is {numbers.half(x)}.
The double of {x} is {numbers.double(x)}''')
e = float(input(f"PERCENTAGE TIME! \nPecentage:"))
print(f'''{e}% of {x} is {numbers.percentange(x, e)}
Adding {e}% of {x} is {numbers.pluspercentage(x, e)}
Subtracting {e}% of {x} is {numbers.minuspercentage(x, e)}''')
