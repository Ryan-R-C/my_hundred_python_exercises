from datetime import date
print("Let's see if your year is in a leap year!")
y = int(input("The year, please. Put 0 to analyze your year."))
if y % 4 == 0 and y % 100 != 0 or y % 400:
    print("Yes!")
if y == 0:
    y = date.today().year
    print("{} is a leap year".format(y))
else:
    print("No,sorry.")