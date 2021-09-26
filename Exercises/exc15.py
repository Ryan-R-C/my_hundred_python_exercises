# MANAGING INPUTS - MATH
# LIBRARY IMPORT

import random
print("Now I'll choose to you a random, three people to a raffle")
n1 = str(input("Here the first"))
n2 = str(input(("Now the second")))
n3 = str(input("Finally the last one"))
laal = [n1, n2, n3]
f = random.choice(laal)
print('The chosen student was {}'.format(f))
