phrase = str(input("Type a phrase:")).strip().upper()
word = phrase.split()
tog = "".join(word)
reverse = tog[::-1]
if reverse == tog:
    print("It's a palindrome!")
else:
    print("It's not a palindrome")
