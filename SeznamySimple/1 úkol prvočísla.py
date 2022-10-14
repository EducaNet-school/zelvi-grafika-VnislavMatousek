volba = int(input("Zadejte číslo:"))
sez = []

for prvocislo in range(volba+1):
    pocet = 0
    if prvocislo < 2:
        continue
    for a in range(2,(prvocislo//2+1)):
        if prvocislo % a == 0:
            pocet = pocet+1
            break
    if pocet == 0 and prvocislo != 1:
        sez.append(prvocislo)
print("Váš seznam prvočísel je:", sez)
