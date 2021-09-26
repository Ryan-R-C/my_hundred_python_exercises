def factorial(n=1, show=False):
    """
    Calculate a factorial of a number.
    :param n: The number that will be calculated the factorial
    :param show: (optional)  It is going to show the math account
    return ...:
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end="")
            if c > 1:
                print(f" x ",end="")
            else:
                print(" = ",end="")
    return f

n = int(input("enter a number to be tranformed to factorial: "))

print(factorial(n))