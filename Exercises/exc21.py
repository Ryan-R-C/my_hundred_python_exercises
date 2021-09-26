#STRINGS

print("Does your name have 'Silva?'")
n = str(input("What's yout name?")).strip()
name = n.upper()
print("So it's {}.".format("SILVA" in name))
