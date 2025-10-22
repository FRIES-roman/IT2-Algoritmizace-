print("program pro zjisteni maxima")

cisla = [3, 7, 7, 2, 7]
n = len(cisla)

maximum = cisla[0]
prvni = 1
posledni = 1
pocet_maxima = 1

for i in range(1, n):
    x = cisla[i]
    if x > maximum:
        maximum = x
        prvni = i + 1
        posledni = i + 1
        pocet_maxima = 1
    elif x == maximum:
        posledni = i + 1
        pocet_maxima += 1

print("maximum je", maximum)
print("prvni vyskyt", prvni)
print("posledni vyskyt", posledni)
print("pocet maxima", pocet_maxima)
