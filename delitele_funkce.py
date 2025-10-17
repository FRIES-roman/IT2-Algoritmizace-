def delitele(n):
    delitele_list = []          
    for i in range(1, n + 1): 
        if n % i == 0:        
            delitele_list.append(i)  
    return delitele_list       

cislo = int(input("Zadej číslo: "))

vysledek = delitele(cislo)
print("Dělitele čísla", cislo, "jsou:", vysledek)
