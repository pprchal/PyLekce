## Lekce 6
## v této lekci si ukážeme další počítání s poli
## zkusíme graf s reprodukčním číslem R 

import sys

import matplotlib.pyplot as plt


def nactiRealneCislo(otazka):
    print(otazka)
    vstup = sys.stdin.readline()
    cislo = float(vstup)
    return cislo

def nactiCeleCislo(otazka):
    print(otazka)
    vstup = sys.stdin.readline()
    cislo = int(vstup)
    return cislo

R = nactiRealneCislo("Zadej číslo R: ")
zacatek = nactiRealneCislo("Zadej aktuální počet: ")
dni = nactiCeleCislo("Zadej počet dní")
osaX = []
osaY = []


nakazenych = zacatek
for den in range(dni):
    osaX.append(den)        # 1,2,3,4,... dni
    osaY.append(nakazenych)
    nakazenych = nakazenych * R


# kreslíme graf       
plt.plot(osaX, osaY)
plt.show()



