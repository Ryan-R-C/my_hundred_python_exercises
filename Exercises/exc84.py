matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = most = scol = 0
for l in range(0, 3):
    for c in range(0,3):
        matrix[l][c] = int(input(f"Type a number to [{l}, {c}] : "))
print("-=-"*20)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matrix[l][c]:^5}]", end="")
        if matrix[l][c] % 2 == 0:
            spar += matrix[l][c]
    print()
print("-=-"*30)
print(f"The sum of the evens is {spar}")
for l in range(0, 3):
    scol += matrix[l][2]
print(f"The sum of the values from the third column is {scol}.")
for c in range(0, 3):
    if c == 0:
        most = matrix[1][c]
    elif matrix[1][c] > most:
        most = matrix[1][c]
print(f"And the greatest number of the second line is {most}")
