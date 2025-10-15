i = 0
Max = 0
vyskyt = 0
prvni = 0
posledni = 0

while True:
    x = int(input("Zadej číslo (-1 = konec): "))
    if x == -1:
        break

    i += 1  

    if i == 1 or x > Max:
        Max = x
        vyskyt = 1
        prvni = i
        posledni = i
    elif x == Max:
        vyskyt += 1
        posledni = i

if i > 0:
    print("\nMaximum:", Max)
    print("První výskyt:", prvni, ". číslo v pořadí")
    print("Poslední výskyt:", posledni, ". číslo v pořadí")
    print("Počet výskytů maxima:", vyskyt)
else:
    print("Nebyla zadána žádná čísla.")
