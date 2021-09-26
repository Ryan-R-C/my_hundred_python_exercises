n1 = float(input("Type your first grade."))
n2 = float(input("Type your second grade."))
m = (n1+n2)/2
if m<6:
    print("I think you need to study more.... {} isn't good!".format(m))
else:
    print("Good grades! {}! Congratulations!".format(m))
