import sys
import math

# výpočet přepony

# začátky - co je co:
# proměnné - kousek v paměti
# typy proměnných (číslo, celé číslo, řetězec-to je libovolný text, datum)
# příkaz je vlastně každý řádek. počítač začne prvním řádkem a pokračuje až do konce

# print vypíše na obrazovku, má 1 vstup, neboli parametr 
print('zadej A')

# = je přiřazení, výsledek zprava vloží do proměnné vstup
# takže sys.stdin.readline() načte vstup z klávesnice a vloží do proměnné vstup
vstup = sys.stdin.readline()
# jenže vstup je text, potřebujeme převést na číslo
a = float(vstup)

print('zadej B')
# nebo můžebe zkrátit, stejné jako řádek 14
b = float(sys.stdin.readline())

# a teď už jenom vypočteme délku přepony
# odmocnina se vypočítá funkcí:   math.sqrt
# [N1]
c = 1
print("Výsledek je: ")
print(c)