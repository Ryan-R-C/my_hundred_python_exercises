list = ('Pen', 1.75,
            'Eraser', 2.00,
            'Notebook', 10.00,
            'Book', 20.00)
print("-"*40)
print("PRICE LIST")
print("-"*40)
for pos in range(0, len(list)):
    if pos % 2 == 0:
        print(f"{list[pos]:.<26}", end=" ")
    else:
        print(f"${list[pos]:>2.2f}\n")
print("-"*40)
