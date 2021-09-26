goal = list()
data = dict()
data["Name"] = str(input("Name of the player:"))
tot = int(input(f"How many games did {data['Name']} play: "))
for c in range(0, tot):
   goal.append(int(input(f" How many goals did {data['Name']} do in the {c+1} game? ")))
data['Goals'] = goal[:]
data["Total"] = sum(goal)
print(data)
print('-=-'*30)
for k,v in data.items():
    print(f"The {k} field has the {v} value")
print('-=-'*30)
print(f"{data['Name']} played {len(data['Goals'])} games.")
for i,v in enumerate(data['Goals']):
    print(f"In the {i+1}° game {data['Name']} did {v} goal(s).")
print(f'Finally, it was a total of {data["Total"]} goals.')