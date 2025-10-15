cislo = int(input("Zadej číslo: "))

if cislo <= 1:
    print(f"{cislo} není prvočíslo.")
else:
    je_prvocislo = True
    for i in range(2, int(cislo**0.5) + 1):
        if cislo % i == 0:
            je_prvocislo = False
            break

    if je_prvocislo:
        print(f"{cislo} je prvočíslo.")
    else:
        print(f"{cislo} není prvočíslo.")
