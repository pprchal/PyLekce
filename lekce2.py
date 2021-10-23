## Lekce 2
import sys
import math

## google: python exit program
## https://www.askpython.com/python/examples/exit-a-python-program
# print tiskne, má 1 parametr
print('zadej A')
vstup = sys.stdin.readline()
a = int(vstup)
if a < 0:
    print("číslo musí být vetší než nula")
    quit()

print('zadej B')
b = int(sys.stdin.readline())

pomoc = (a*a)+(b*b)
c = math.sqrt(pomoc)

print("Výsledek je: ")
print(c)