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

# print('zadej A')
# vstup = sys.stdin.readline()
# a = int(vstup)
a = nactiCislo('zadej A')

# print('zadej B')
# b = int(sys.stdin.readline())
b = nactiCislo('zadej B')

# pomoc = (a*a)+(b*b)
# c = math.sqrt(pomoc)
c = pythagor(a, b)

# tady je použit trik - formátování výstupu
# je to taková šablona, kde se za %f dosadí číslo
# nemusíš to pamatovat, stačí zagooglit
# https://tutorial.eyehunts.com/python/python-print-format-float-example-code/
print("Výsledek je: %f", c)
# print(c)

