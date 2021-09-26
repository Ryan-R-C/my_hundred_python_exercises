def lal(msg):
    t = len(msg) + 4
    print("~"*t)
    print(f"  {msg}")
    print("~"*t)

name = str(input("Your message: "))

lal(name)