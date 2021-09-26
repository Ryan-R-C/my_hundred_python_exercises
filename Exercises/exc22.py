#STRINGS
x = str(input("Type a phrase here.")).strip().upper()
phrase_a_s = x.count("A")
laal = x.find("A")+1
print("There's {} A(s) in your phrase".format(phrase_a_s))
print("The fist 'A' appeared in {} position".format(laal))
print("The last 'A' is in {}".format(x.rfind("A")+1))
