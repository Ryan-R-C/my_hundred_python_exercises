s = olderman = 0
oldername = ''
totunderwoman = 0
for c in range(1, 5):
    print('-_-_-_-{}-_-_-_-'.format(c))
    name = str(input("Type here the name of person:")).strip()
    age = int(input("The age:"))
    s += age
    sex = str(input("The sex [M/F]:")).upper().strip()
    if c == 1 and sex == "M":
        age = olderman = age
        name = oldername
    if sex == "M" and age > olderman:
        oldername = name
        olderman = age
    if sex == "F" and age < 20:
        totunderwoman += 1
media = s/4
print("The media age of this people is {}." .format(media))
print("The older man is {} years old. His name is {}".format(olderman, oldername))
print("There is {} woman under 20 years.".format(totunderwoman))