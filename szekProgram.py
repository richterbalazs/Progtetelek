from Osztaly import Szek

peldany1 = Szek("kék", 3)
peldany2 = Szek("piros", 4)
peldany3 = Szek("zöld", 5)
print(peldany1.__str__())
print(peldany2)
print(peldany3)

szekek = [peldany1, peldany2, peldany3]

def lab_megszamlalas():
    print("Összesen hány lába van a székeknek?")
    osszeg = 0
    for index in range(0, len(szekek), 1):
        osszeg += szekek[index].labszam
    print(f"Összesen: {osszeg}")

lab_megszamlalas()

def maxLabSzin():
    maxIndex = 0
    for index in range(1, len(szekek), 1):
        if szekek[index].labszam > szekek[maxIndex].labszam:
            maxIndex = index
    print(f"A legtöbb lábbal rendelkező szék színe: {szekek[maxIndex].szin}")

maxLabSzin()