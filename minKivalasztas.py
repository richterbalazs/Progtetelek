def minKivalasztas():

    VEGE = 0
    db = 0
    min = 2147483647
    while (szam := int(input("N="))) != VEGE:
        if szam < min:
            min = szam
        db += 1
    print(f"{db} számból a legkisebb: {min}")