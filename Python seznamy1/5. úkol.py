
sez = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět", "deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct", "dvacet", "dvacet jedna", "dvacet dva", "dvacet tři", "dvacet čtyři", "dvacet pět", "dvacet šest", "dvacet sedm", "dvacet osm", "dvacet devět", "třicet", "třicet jedna", "třicet dva", "třicet tři", "třicet čtyři", "třicet pět", "třicet šest", "třicet sedm", "třicet osm", "třicet devět", "čtyřicet", "čtyřicet jedna", "čtyřicet dva", "čtyřicet tři", "čtyřicet čtyři", "čtyřicet pět", "čtyřicet šest", "čtyřicet sedm", "čtyřicet osm", "čtyřicet devět","padesát", "padesát jedna", "padesát dva", "padesát tři", "padesát řtyři", "padesát pět", "padesát šest", "padesát sedm", "padesát osm", "padesát devět", "šedesát", "šedesát jedna", "šedesát dva", "šedesát tři", "šedesát čtyři", "šedesát pět", "šedesát šest", "šedesát sedm", "šedesát osm", "šedesát devět", "sedmdesát","sedmdesát jedna","sedmdesát dva","sedmdesát tři","sedmdesát čtyři", "sedmdesát pět","sedmdesát šest","sedmdesát sedm", "sedmdesát osm", "sedmdesát devět","osmdesát","osmdesát jedna","osmdesát dva","osmdesát tři","osmdesát čtyři","osmdesát pět", "osmdesát šest", "osmdesát sedm", "osmdesát osm", "osmdesát devět","devadesát","devadesát jedna", "devadesát dva", "devadesát tři", "devadesát čtyři", "devadesát pět", "devadesát šest", "devadesát sedm", "devadesát osm", "devadesát devět"]

volba = int(input("Zadejte číslo od 0 do 99:"))

if volba < 0 or volba > 99:
    print("Byla zadána hodnota mimo interval 0 až 99")

print("Vaše číslo je:", volba)
print(sez[volba])

