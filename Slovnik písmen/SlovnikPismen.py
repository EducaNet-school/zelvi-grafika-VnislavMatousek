def vypocet():
    volba = input("Zadejte větu:")
    slovo = False
    for znak in volba:
        if znak in volba:
            if znak in "=´)§¨,.-%ˇ!'?:_":
                print("Zadej větu bez těchto znaků: =´)§¨,.-%ˇ!'?:_ ")
                break
#uživatel zadá větu pokud zada nejaky špatný znka např. !, tak se program vypne
#poté co zadá větu správně tak program dá jeho větu bez mezer a promění velka pismena na mala a pote spocita a seradi podle abecedy
    volba = volba.lower()
    volba = ("%s" % (''.join(volba.split(' '))))
    cisla = {
#výsledek není psaný ve složených závorkách, je to kvůli tomu, sort příkazu, ale stále je to slovník
    }
    for a in volba:
        pocet = cisla.keys()
        if a in pocet:
            cisla[a] += 1
        else:
            cisla[a] = 1
    cisla = sorted(cisla.items())
    print(cisla)
vypocet()
