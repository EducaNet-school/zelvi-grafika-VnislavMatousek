
seznam = []
volba = input("Zadejte první číslo:")
seznam.append(volba)
volba1 = input("Zadejte druhé číslo:")
seznam.append(volba1)
volba2 = input("Zadejte třetí číslo:")
seznam.append(volba2)
volba3 = input("Zadejte čtvrté číslo:")
seznam.append(volba3)
volba4 = input("Zadejte páté číslo:")
seznam.append(volba4)


max = seznam[0]

for a in seznam:
    if a  > max:
        max = a
print("Největší číslo je", max)


