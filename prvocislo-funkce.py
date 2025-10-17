cislo = int(input("Zadej číslo: "))

if cislo < 2:
    print(f"{cislo} není prvočíslo.")
else:
    i = 2
    je_prvo = True
    while i * i <= cislo:
        if cislo % i == 0:
            je_prvo = False
            break
        i += 1
    if je_prvo:
        print(f"{cislo} je prvočíslo.")
    else:
        print(f"{cislo} není prvočíslo.")
