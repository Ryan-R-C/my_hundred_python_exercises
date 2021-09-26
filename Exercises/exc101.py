def readint(msg):
    x = str(input(msg)).strip()
    while True:
        if x.isnumeric():
            print(f"\nYou typed {x}.")
            break
        else:
            print("\033[0;31mError! Type a integer number.\033[m")
            x = str(input("Please, type a integer: ")).strip()

n  = readint("Type a number:")