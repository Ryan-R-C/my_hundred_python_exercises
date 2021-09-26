from datetime import datetime
data = dict()
data["Name"] = str(input("Your name: "))
age = int(input("Year you was born:"))
data["Age"] = datetime.now().year - age
data["Work card"] = int(input("Your work card [type 0 if you don't have]:"))
if data["Work card"] == 0:
    for k, v in data.items():
        print(f"{k} = {v}")
else:
    data["Year hired"] = int(input("Your year hired: "))
    data["Salary"] = float(input("Your salary: $"))
    data["Retirement"] = (data["Year hired"] + 35 - datetime.now().year) + data["Age"]
    for k, v in data.items():
        print(f"{k} = {v}")
