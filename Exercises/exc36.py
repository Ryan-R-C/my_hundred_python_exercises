print("Today we'll see if you were accredited!")
print('''Our system is:
 If your final media is lower than 5 - Disapproved
 Your final media between 5.0 and 6.9 - Recuperation
 And finally bigger than 7 - Okay''')
notea = float(input("Type here your first note."))
noteb = float(input("Now the last."))
final = ((notea+noteb)/2)
if final < 5:
    print("Disapproved! How shame!")
elif 5 <= final <= 6.9:
    print("Recuperation! I'll see ya on the your vacations! HA HA HA!")
else:
    print("You're Okay!")