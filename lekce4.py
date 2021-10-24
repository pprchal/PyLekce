## Lekce 4
## v této lekci si ukážeme smyčky - opakování příkazů

## https://www.educba.com/do-while-loop-in-python/





# napřed úplně základní smyčka
# opakuje příkazy po dvojtečce
# úkol: 
for k in range(5):
    print("ahoj")



# nebo jiná možnost
i = 1
while True:         # dokud platí podmínka, opakuj od A do C
    print(i)        # A
    i = i + 1       # B
    if(i > 5):      # C
        print("Končím, už toho bylo dost.")   # C1
        break                                 # C2

