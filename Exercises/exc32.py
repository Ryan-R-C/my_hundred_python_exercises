print("Today's exercise is about loan of your house!")
house = int(input("Type here the value of house, please."))
salary = int(input("Here your monthly salary."))
years = int(input("And, finally, how many year you want to divide the whole value."))
x = salary*0.03
ac = house/years
laal = house / (years*12)
if x > ac:
    print("Sorry, you aren't on your scale.")
    print("The minimal would be {}".format(ac))
else:
    print("Yes you can! It'll cost {} by each month".format(laal))
