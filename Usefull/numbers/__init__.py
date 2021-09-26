
def half(n, formata=False):
    q = (n/2)
    if formata is True:
        return coin(q)
    else:
        return q


def double(n, formata=False):
    w = (n*2)
    if formata is True:
        return coin(w)
    else:
        return w

def percentange(n, e=100, formata=False):
    r = n * (e/100)
    if formata is True:
        return coin(r)
    else:
        return r


def pluspercentage(n, e=100, formata=False):
    t = n + (n*(e/100))
    if formata is True:
        return coin(t)
    else:
        return t

def minuspercentage(n, e=100, formata=False):
    y = n - (n*(e/100))
    if formata is True:
        return coin(y)
    else:
        return y

def coin(n=0, m="USD"):
    return f'{m} {n:.2f}'#.replace('.',',')

def summary(n, e):
    print("-"*30)
    y = ("Summary of the values!").center(30)
    print(y)
    print("-"*30)
    print(f"Number:{n}.")
    print(f"Double:{double(n, formata=True)}.")
    print(f"Half:{half(n, formata=True)}.")
    print(f"Subtracting {e}% {n} of is {minuspercentage(n, e, formata=True)}.")
    print(f"Adding {e}% of {n} is {pluspercentage(n, e, formata=True)}.")
    print("-" * 30)

def isvalid(msg):
    valid = False
    while not valid:
        try:
            price = str(input(msg)).replace(",", ".").strip()
            if msg.isalpha():
                print(f"ERROR! \"{price}\" is not a valid number! ")
            else:
                valid = True
                return float(price)
        except:
            print("SOMETHING WENT WRONG")

def readint(msg):
    while True:
        try:
                i = int(input(msg))
        except (ValueError, TypeError):
            print("ERROR! Please type an integral number.")
            continue
        except (KeyboardInterrupt):
            print("The user did not want to inform it's data")
            return 0
        else:
            return i

def readfloat(msg):
    while True:
        try:
            f = float(input(msg))
        except (ValueError, TypeError):
            print("ERROR! Please type a floating number.")
            continue
        except (KeyboardInterrupt):
            print("The user did not want to inform it's data")
            return 0
        else:
            return f