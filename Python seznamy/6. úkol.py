seznam = ["Michael Schumacher", "Max verstapen", "Sebastian Vettel"]
print("Toto jsou jména závodníků",seznam)
volba = input("Zadejte nové jméno závodníka:")
seznam.append(volba)
print(seznam)
volba2 = input("Vyberte, které jméno chcete smazat pomocí čísel od 0 do 3:")
if(volba2 == "0"):
    del seznam[0]
    print("Vymazal jste jméno Michael Schumacher.","Toto jsou vaše zbývající jména:", seznam)
if(volba2 == "1"):
    del seznam[1]
    print("Vymazal jste jméno Max Verstapen.","Toto jsou vaše zbývající jména:", seznam)
if(volba2 == "2"):
    del seznam[2]
    print("Vymazal jste jméno Sebastian Vettel.","Toto jsou vaše zbývající jména:", seznam)
if(volba2 == "3"):
    del seznam[3]
    print("Vymazal jste vaše jmeno",volba,".", "Toto jsou vaše zbývající jména:",seznam)

pocet = len(seznam)
print("Počet jmen je:",pocet)

seznam.sort()
print("Toto jsou vaše zadaná jména seřazená podle abecedy.",sorted(seznam))
