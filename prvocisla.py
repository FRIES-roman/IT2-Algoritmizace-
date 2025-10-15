cislo = int(input("Zadej číslo: "))

if cislo > 1:
    for i in range(2, int(cislo**0.5) + 1):
        if cislo % i == 0:
            print(f"{cislo} není prvočíslo.")
            break
    else:
        print(f"{cislo} je prvočíslo.")
else:
    print(f"{cislo} není prvočíslo.")
