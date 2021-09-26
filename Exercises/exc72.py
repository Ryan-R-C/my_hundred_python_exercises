x = (int(input("Type the fist number here:")),
int(input("Type the fist number here:")),
int(input("Type the fist number here:")),
int(input("Type the fist number here:")))
print(f'''You typed {x}.''')
if 3 in x:
    print('The number three appeared in {x.index(3)+1}° postion, at first time!')
else:
    print("The number 3 was not typed.")
print(f'''The number nine appeared {x.count(9)} time(s).
And the evens numbers were:''', end=" ")
for n in x:
    if n % 2 == 0:
        print(n, end=" ")
