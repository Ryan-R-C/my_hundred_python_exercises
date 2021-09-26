
def vote(year = 0):
    from datetime import date
    x = date.today().year
    parameter = x-year
    print(parameter)
    if parameter < 18:
        print("You are underage.")
        if 18 > parameter > 16:
            print("Your vote is optional! ")
        else:
            print("You do not vote, my son.")
    elif 70 > parameter > 18:
        print("Your vote is compulsory! ")
    else:
        print("Your vote is optional.")

a = int(input("Type the year you have born: "))
vote(a)
