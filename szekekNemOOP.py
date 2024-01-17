def szekinit(szin:str, labszam:int):
    print(f"Szék: {szin}, Láb: {labszam}")

szekinit("kék",3)
szekinit("piros",4)
szekinit("zöld",5)

def szekstr(szin:str, labszam:int):
    return (f"Szín: {szin}, Lábszám: {labszam}")

print(szekstr("kék",3))
print(szekstr("piros",4))
print(szekstr("zöld",5))