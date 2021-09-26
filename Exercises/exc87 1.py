data = {}
data["Name"] = str(input("Name: "))
data["Average"] = float(input(f"Average of {data['Name']}: "))
if data["Average"] >= 7:
    data["Situation"] = "Approved!"
elif 5 <= data["Average"] < 7:
    data["Situation"] = "educational recuperation"
else:
    data["Situation"] = "failed"
print("-=-"*30)
for k,v in data.items():
    print(f"{k} is {v}.")