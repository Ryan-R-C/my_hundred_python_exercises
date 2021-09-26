def notesread(*n, sit=False):
    r = dict()
    r["Total"] = len(n)
    r["Greater number"] = max(n)
    r["Lesser number"] = min(n)
    r["Average"] = sum(n)/len(n)
    if sit:
        if r["Average"] >= 7:
            r["Situation"] = "Good"
        elif r["Average"] >= 5:
            r["Situation"] = "Middling"
        else:
            r["Situation"] = "POOR!"
    return r


anw = notesread(5, 10, 6, sit=True)
print(anw)