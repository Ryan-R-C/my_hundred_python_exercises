def goalcalc():
    q = str(input("Name of player: ")).strip()
    w = str(input("How many goals: ")).strip()
    if q == "":
        q = "<Unknown>"
    if w == "":
        w = "0"
    if w != "1" and w != "one":
        print(f"Player {q} did {w} goals")
    else:
        print(f"Player {q} did {w} goal.")

goalcalc()