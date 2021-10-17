import sys
import math


def pythagor(a, b):
    pomoc = (a*a)+(b*b)
    return math.sqrt(pomoc)

# print tiskne, má 1 parametr
print('zadej A')
vstup = sys.stdin.readline()
a = int(vstup)

print('zadej B')
b = int(sys.stdin.readline())

c = pythagor (a, b)
print("Výsledek je: ")
print(c)