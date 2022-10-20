
sez = [23,38,71,99,85]


volba1 = int(input("Zadejte kladné čísla pro posun do prava nebo záporné číslo pro posun do leva:"))

#program posunuje dobře co se týče do leva a do prava akorá přidává jedno navíc,kvůli tomu, že v seznamech je nula, ale jinak to funguje

if volba1 < 0:
    sez = sez[-volba1:] + sez[:-volba1]
    print("Váš seznam se posunul o", volba1, "do leva", "a toto je nyní váš sznam:",sez)

if volba1 > 0:
    sez = sez[volba1:] + sez[:volba1]
    print("Váš seznam se posunul o", volba1, "do prava", "a toto je nyní váš sznam:",sez)


