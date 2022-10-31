sez = [24,36,98,50,48,12,96,100,120,15,45]

volba = int(input("Zadejte číslo, podle kterého bude program určovat jstli jsou čísla v seznamu větší než číslo vámi zadané:"))


for a in sez:
    if a < volba:
        print("Nepravda, některá čísla jsou menší než vámi zadané")
    elif a > volba:
        print("Pravda všechny čísla jsou větší než vámi zadané číslo")
    break

