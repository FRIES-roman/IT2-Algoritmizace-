n = int(input("Zadej počet čísel: "))

x = int(input("Zadej 1. číslo: "))
Max = x
pocet = 1
prvni = 1
posledni = 1

for i in range(2, n + 1):
    x = int(input(f"Zadej {i}. číslo: "))

    if x > Max:
        Max = x
        pocet = 1
        prvni = i
        posledni = i
    elif x == Max:
        pocet += 1
        posledni = i

print(f"\nMaximum: {Max}")
print(f"První výskyt: {prvni}. číslo v pořadí")
print(f"Poslední výskyt: {posledni}. číslo v pořadí")
print(f"Počet výskytů maxima: {pocet}")