#STRINGS

print('Now all the letters of your will be: \n Fist lowercase \n Second uppercase \n And after it all -How many letter there is in your whole name and first-.')
name = str(input('Put here your whole name please.')).strip()
up_name = name.upper()
low_name = name.lower()
print('Your name whole uppercase {}.'.format(up_name))
print('Your name whole lowercase is {}.'.format(low_name))
whole = len(name) - name.count(' ')
print("Your name have {} letters.".format(whole))
divide = name.split()
print("You fist name have {} letters".format(len(divide[0])))
