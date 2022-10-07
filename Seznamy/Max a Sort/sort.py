seznam = [3, 2,55 , 1]
seznam2 = []

def sort(seznam):
    while seznam:
        nejmensi = seznam[0]
        for i in seznam:
            if i < nejmensi:
                nejmensi = i
        seznam2.append(nejmensi)
        seznam.remove(nejmensi)
    return seznam2

sort(seznam)
print(seznam2)

    
