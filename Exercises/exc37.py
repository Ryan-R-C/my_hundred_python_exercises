from datetime import date
print("Let's see category you're")
birth = int(input("Type here which year you born"))
y = date.today().year
laal = y-birth
print("And your category is:")
if laal <= 9:
    print("Little")
elif 9 < laal <= 14:
    print("Childlike")
elif 14< laal <= 19:
    print("Junior")
elif 19 < laal < 20:
    print("Senior")
else:
    print("Master")