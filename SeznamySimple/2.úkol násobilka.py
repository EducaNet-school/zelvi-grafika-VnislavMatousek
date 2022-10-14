volba = int(input("Zadejte číslo od 2-10, které chcete násobit: "))

sez = []

for i in range(1,10+1):
    nasobek = volba*i
    sez.append(nasobek)
print("Váš seznam násobků je:",sez)
