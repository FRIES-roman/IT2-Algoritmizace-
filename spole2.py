print("program pro zjisteni maxima")

cisla = [1, 6, 3, 7, 8, 6, 8, -1]

if cisla[0] == -1:
    print("Nebyla zadana žádná čísla.")
else:
    maximum = cisla[0]
    prvni = 1
    posledni = 1
    pocet_maxima = 1
    i = 1

    for x in cisla[1:]:
        if x == -1:
            break
        i += 1
        if x > maximum:
            maximum = x
            prvni = i
            posledni = i
            pocet_maxima = 1
        elif x == maximum:
            posledni = i
            pocet_maxima += 1

    print("maximum je:", maximum)
    print("prvni vyskyt:", prvni)
    print("posledni vyskyt:", posledni)
    print("pocet maxima:", pocet_maxima)
