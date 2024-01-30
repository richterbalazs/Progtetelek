import math

def oszthato(szam):
    lista = []
    for oszto in range(2, round(math.sqrt(szam)+1)):
        if szam % oszto == 0:
            lista.append(oszto)
    return lista

print(oszthato(10007))

def masodik(szam):
    lista = []
    oszto = 2
    while oszto <= math.sqrt(szam):
        if szam % oszto == 0:
            lista.append(oszto)
        oszto += 1
    return lista

print(masodik(36))