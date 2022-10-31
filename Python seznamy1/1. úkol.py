
volba = int(input("Zadejte číslo: "))

sez = [1,3,5,7,9,11,13,15,17,19]


if volba % 2 == 0:
   print("Vaše číslo",volba,"je sudé")
   print("Největší liché číslo nejbližší k vašemu číslu je:", volba+1)
   for cislo1 in range(1,11):
       if cislo1 % 2 != 0:
        sez.append(volba+1)
        sez.append(cislo1)
        celkem = sum(sez)
        celkem1 = len(sez)
        celkem2 = float(celkem/celkem1)
   print("Váš průměr:",round(celkem2,2))
   print("Váš seznam byl:",sez)


if volba % 2 != 0:
    print("Vaše číslo",volba,"je liché")
    for cislo2 in range(1, 17 + 1):
        if cislo2 % 2 != 0:
         sez.append(cislo2)
         celkem3 = sum(sez)
         celkem4 = len(sez)
         celkem5 = float(celkem3/celkem4)
    print("Váš průměr:",round(celkem5,2))
    print("Váš seznam byl:",sez)



