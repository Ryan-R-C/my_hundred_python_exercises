
print("I'll show to you your first and last name.")
a = str(input("Type your name here, please.")).strip().title()
name = a.split()
print("Your first name is {}.".format(name[0]))
print("Your last name is {}.".format(name[len(name)-1]))

