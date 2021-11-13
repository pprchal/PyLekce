# Python lekce programování

## lekce1.py - výpočet přepony trojůhelníka
> Začátky, načtení vstupu, tisk na obrazovku.

Má spoustu chyb, ale ty budou opraveny v dalších lekcích.
Třeba počítá přeponu ze záporného čísla.

## lekce2.py - příkaz if, větvení
> Oprava záporných vstupů

## lekce3.py - funkce
> Vytvoření funkce pro výpočet přepony

> Vytvoření funkce pro vstup čísla

## lekce4.py - smyčky 
> Základy opakování programu


## lekce5.py - smyčky a kreslení
> Trochu obtížnější

> Výstupem by ale měl být hezký graf funkce sinus

# Nápovědy
## N1
```py
pomoc = (a*a)+(b*b)
c = math.sqrt(pomoc)
```

## N2
```
if a <= 0:
    print("číslo A musí být vetší než nula")
    quit()
```

## N3
```
if b <= 0:
    print("číslo B musí být vetší než nula")
    quit()
```

## N4
```
def nactiCislo(otazka):
    print(otazka)
    vstup = sys.stdin.readline()
    cislo = float(vstup)
    if vislo <= 0:
        print("číslo musí být vetší než nula")
        quit()
    return cislo
```

