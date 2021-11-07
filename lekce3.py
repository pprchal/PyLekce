## Lekce 3
## v této lekci si ukážeme funkce.
## v komentáři je kód z předchozí lekce
import sys
import math

# přidej kontrolu na nezáporné číslo
def pythagor(a, b):
    pomoc = (a*a)+(b*b)
    c = math.sqrt(pomoc)    
    return c

def nactiCislo(otazka):
    print(otazka)
    vstup = sys.stdin.readline()
    cislo = int(vstup)
    return cislo

# pokaždé by se muselo psát znova a znova - funkce nactiCislo
# print('zadej A')
# vstup = sys.stdin.readline()
# a = int(vstup)
a = nactiCislo('zadej A')

# pokaždé by se muselo psát znova a znova - funkce nactiCislo
# print('zadej B')
# b = int(sys.stdin.readline())
b = nactiCislo('zadej B')

# pokaždé by se muselo psát znova a znova - funkce pythagor
# pomoc = (a*a)+(b*b)
# c = math.sqrt(pomoc)
c = pythagor(a, b)

# tady je použit trik - formátování výstupu
# je to taková šablona, kde se za %f dosadí číslo
# nemusíš to pamatovat, stačí zagooglit
# https://stackoverflow.com/questions/55048668/how-to-print-a-float-variable-using-the-formatting#55048887

# print(c)    # vypíše # 22.360679774997898


print(f"Výsledek je: {c:.2f}")  

