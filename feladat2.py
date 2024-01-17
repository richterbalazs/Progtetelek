import math

n = (int(input("N= ")))
prim = bool
i = 2

if n < 2:
    prim = False
else:
    while i < n and n % i == 0:
        i = i

prim = i > math.sqrt(n)

print(f"{prim}, Nem prím")