print("Today we're going to show to you the sum of your six values, but if it be odds we'll disconsider.")
sum = 0
cont = 0
for c in range(1,7):
    num = int(input("Type the {}° number".format(c)))
    if num % 2 == 0:
        sum += num
        cont += 1
print("You informed {} evens numbers and the sum of they all is {}".format(cont, sum))
