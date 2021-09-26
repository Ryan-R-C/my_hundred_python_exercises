most = 0
less = 0
for c in range(1, 6):
    i = int(input("Type here the weight of a person:"))
    if c == 1:
        most = i
        less = i
    else:
        if i > most:
            most = i
        if i < less: ###This here is to see if the weight is less than the other
            less = i
print("The greater weight was {} and the lower weight was {}.".format(most, less))