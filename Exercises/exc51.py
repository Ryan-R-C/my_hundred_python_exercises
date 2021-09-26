from datetime import date
today = date.today().year
count = 0
totadult = 0
totunder = 0
for c in range(1,8):
    i = int(input("Type here which the {}° person has born:".format(c)))
    age = i - today
    if age >= 21:
        totadult += 1
    else:
        totunder += 1
print("From what you type: {} person(s) adult and {} person(s) under age.".format(totadult, totunder))

