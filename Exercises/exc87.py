data = dict()
n = str(input("Name:"))
a = int(input(f"Average of {n}: "))
data['Name'] = n
data['Average'] = a
if a < 5:
    data["Situation"] = "failed"
elif 5 <= a < 7:
    data["Situation"] = "educational recuperation"
else:
    data["Situation"] = "Approved!"
for k, v in data.items():
    print(f"    - {k} is {v}")