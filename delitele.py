n = int(input("Zadej číslo: "))
delitele_list = []

for i in range(1, n + 1):
    if n % i == 0:
        delitele_list.append(i)

print(f"Dělitele čísla {n} jsou: {delitele_list}")
