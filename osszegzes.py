def feladat():
    n =int(-1)
    i = int()

    while n < 0:
        print("N = ", end="")
        n = int(input())
    ossz = 0
    for i in range(1, n+1, 1):
        ossz += i
    print(f"Az első {n} természetes szám összege: {ossz}")






