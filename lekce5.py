## Lekce 4
## v této lekci si ukážeme smyčky - opakování příkazů
## vypíšeme funkci sin

## najeď myší nad funkci sin
## objeví se nápověda - measured in radians


## dokumentace kreslení:
## https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html

import sys
import math

import matplotlib.pyplot as plt

# nauč se sám - listy, seznamy
# https://www.w3schools.com/python/python_lists.asp
osaX = []
osaY = []

kroku = 20
kousekX =  (2 * math.pi) / kroku        # počítáme 360 stupňů...
hlaska = "kousekX: " + str(kousekX)     # sečtení jablko a jablko -- str() převede číslo na řetězec
print(hlaska)
x = 0
for krok in range(kroku):
    osaX.append(x)
    y = math.sin(x)
    osaY.append(y)

    x = x + kousekX
    druhaHlaska = "krok[" + str(krok) + "] X: " + str(x) + "Y: " + str(y)
    print(druhaHlaska)


#        
plt.plot(osaX, osaY, 'ro')
# plt.axis([0, 6, 0, 20])
plt.show()

# Data for plotting
# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2 * np.pi * t)

# fig, ax = plt.subplots()
# ax.plot(t, s)

# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        title='About as simple as it gets, folks')
# ax.grid()

# fig.savefig("test.png")
# plt.show()



