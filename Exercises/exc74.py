words = ("learn", "progamation", "language", "python", "free", "pratice", "future")
for w in words:
    print(f"\nIn the word {w.capitalize()} we have: ", end=" ")
    for letter in w:
        if letter.lower() in "aeiou":
            print(letter, end=" ")