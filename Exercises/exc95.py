from time import sleep

def x(msg):
    t = len(msg) + 4
    print("~"*t)
    print(f"  {msg}")
    print("~"*t)

def cont(a, b, c):
    print(f"Counting from {a} to {b}, {c} in {c}")
    if a >= b:
        while b <= a:
            print(a, end = " ", flush=True)
            sleep(0.1)
            a -= c
        print(".")
        print()
    else:
        while a <= b:
            print(a,  end=" ", flush=True)
            sleep(0.2)
            a += c
        print(".")
        print()
x("Exercise: 98")
cont(0, 10, 1)

cont(10, 0, 2)

print("Now, You Choose!")
q = int(input("Begin: "))
w = int(input("End: "))
e = int(input("Step: "))
if e < 0:
    e *= (-1)
elif e == 0:
    e = 1
cont(q, w, e)