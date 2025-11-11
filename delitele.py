n = int(input("Zadej číslo: "))

print(f"Dělitele čísla {n} jsou:", end=" ")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")

