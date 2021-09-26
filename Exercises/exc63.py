n = cont = s = 0

while True:
    n = int(input('''The computer will stop when you type 999.
Type a number:'''))
    if n == 999:
        break
    cont += 1
    s += n
print(f"The sum of all your numbers is {s}. And you typed {cont} numbers.")