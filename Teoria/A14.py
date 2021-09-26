'''forc in range (1,11):
    print(c)'''
c = 1
while c < 11:
    print(c)
    c += 1
print("END")
n = 1
while n != 0:
    n = int(input("Type a number:"))
print("END")
r = "S"
while r == "S":
    n = int(input("Type a number:"))
    r = str(input("Do you wanna try again?[S/N]")).upper()
