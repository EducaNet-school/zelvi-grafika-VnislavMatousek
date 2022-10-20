volba = int(input("Zadejte číslo:"))

sez = []

x,y=0,1

while y<volba:
    sez.append(y)
    x,y = y,x+y
print("Posloupnost je:",sez)

