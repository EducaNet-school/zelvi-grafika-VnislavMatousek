


# uživatel zadá minimalní a maximalní číslo
volba1 = int(input("Zadejte minimální číslo:"))
volba2 = int(input("Zadejte max číslo:"))

sez = []
#program mezi těmito dvěma čísly vybere všechny lichá čísla
for num in range(volba1, volba2 + 1):
    if num % 2 != 0:
        sez.append(num)
        celkem = sum(sez)
print("lichá čísla jsou:", sez)
print("Celkem tyto čísla jsou:",celkem)
#a poté program je zapíše do seznamu a sečte je

volba3 = int(input("Zadejte minimální hodnotu:"))
volba4 = int(input("Zadejte max hodnotu:"))
#tady to funguje stejně, prostě to vygeneruje další lichá čísla

sez1 = []

for num1 in range(volba3,volba4 + 1):
    if num1 % 2 != 0:
        sez1.append(num1)
        celkem1 = sum(sez1)
print("Lichá čísla jsou:", sez1)
print("Celkem tyto čísla jsou:", celkem1)


print("A celkem jsou všechna lichá čísla v programu celkem", celkem + celkem1)
#ke konci program sečte lichá čísla s obou programů



