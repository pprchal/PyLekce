## Lekce 2 - podmínky
import sys
import math

## google: python exit program
## https://www.askpython.com/python/examples/exit-a-python-program
# print tiskne, má 1 parametr
print('zadej A')
vstup = sys.stdin.readline()
a = float(vstup)

# if je podmíněný příkaz. to znamená, že řádky 15 a 16 se provedou jen když
# bude platit, že a < 0
if a <= 0:
    print("číslo A musí být vetší než nula")
    quit()   # speciální funkce - ukončí celý program

print('zadej B')
b = float(sys.stdin.readline())
# napiš program tak, aby číslo B nemohlo být menší než nula
# [N2]

pomoc = (a*a)+(b*b)
c = math.sqrt(pomoc)

print("Výsledek je: ")
print(c)