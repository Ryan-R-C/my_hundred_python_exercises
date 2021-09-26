from datetime import date
print("Hello, my young! Let's see if you'll serve your country at Army!")
birth = int(input("So... In which year do you birth?"))
y = date.today().year
laal = y-birth
x = laal-18
if 18 > laal:
    print("Your time is coming up. HA HA HA! {} year(s) go through quickly!".format(x))
elif laal > 18:
    print("No sir, Your time already has been passed!. It has been {} years.".format(x))
else:
    print("Hoom, This year you need to list yourself at army!")