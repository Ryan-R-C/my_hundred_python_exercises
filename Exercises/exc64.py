i = x = 0
while True:
    print("-=-"*20)
    i = int(input('''Type here a number and I'll show to you its Multiplication Table. The computer will stop if you type a negative number
Your number:'''))
    print("-=-" * 20)
    if i >= x:
        for c in range(1, 11):
            print('{} x {} = {}'.format(i, c, c*i))
    else:
        break
print("End, Thanks!")

