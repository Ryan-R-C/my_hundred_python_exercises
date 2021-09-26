def factorial(n):
    f=1
    for c in range(1, n+1):
        f *= c
    return f

num = int(input("Type a number: ")
fact = factorial(num)
print(f"The factorial of {num} is {fact}.")