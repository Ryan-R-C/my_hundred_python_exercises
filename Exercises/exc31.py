print("Hey there! Today we'll se your salary increase")
a = int(input("Type here your salary, please."))
if a >= 1250:
    salary = a + 10*(a/100)
else:
    salary = a + 15*(a/100)
print("Your new salary is {}!".format(salary))
