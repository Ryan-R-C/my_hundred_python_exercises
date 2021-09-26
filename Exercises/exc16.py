# MANAGING INPUTS - MATH
# LIBRARY IMPORT

import random
print("Now I'll randomize a list.")
n1 = str(input("Type here the fist."))
n2 = str(input("The second."))
n3 = str(input("The third."))
n4 = str(input("The last one."))
n = [n1, n2, n3, n4]
random.shuffle(n)
print("The list chosen was")
print(n)
