print("Today: Body mass index.")
print('''Note:
1 Kilogram is equal to 2.20462 pounds
1 Metre is equal to 3.28084 foot or 39.3701 Inches''')
a = float(input("Type here your weight (in Kg)."))
b = float(input("And here your height (in m)."))
bmi = a / (b ** 2)
print("Your Body mass index is {:.1f} And you're on your".format(bmi), end='')

if bmi < 18.5:
    print(" Below normal weight.")
elif 18.5 <= bmi < 25:
    print(" Normal weight")
elif 25 <= bmi <= 30:
    print(" Overweight")
elif 30 < bmi <= 40:
    print(" I Obesity")
else:
    print(" Morbid obesity. Take care!")
    