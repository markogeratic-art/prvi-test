#
# Vrne tisti element tabele <x> v tabeli, pri katerem je vrednost funkcija(x) najmanjša.
#
def minimum(tabela, funkcija):
    
    najmanjsi = tabela[0]
    f_najmanjsi = funkcija(najmanjsi)


    for i in range(1, len(tabela)):
        f_trenutni = funkcija(tabela[i])
        if f_trenutni < f_najmanjsi:
            najmanjsi = tabela[i]
            f_najmanjsi = f_trenutni

    return najmanjsi

def kvadrat(x):
    return x ** 2

def nasprotna(x):
    return -x

t = [-7, 6, 9, -3, -8, 4, -5, -2, -6, -4]
print(minimum(t, kvadrat))
print(minimum(t, nasprotna))

def element_na_indexu(index):
    return t[index]

indexi = []
for i in range (len(t)):
    indexi.append(i)

print(minimum(indexi, element_na_indexu))

#krajše:
indexi = list(range(len(t)))

imena = ['Denis', 'Franci', 'Gabrijela', 'Andreja', 'Hana', 'Cvetka', 'Eva', 'Bojan']
print(min(imena))
print(max(imena))
print(minimum(imena, lambda ime: len(ime)))
print(min(imena, key=lambda ime: len(ime)))
print(min(imena, key=lambda ime: -len(ime)))

print(sorted(imena))
print(sorted(imena, key=lambda ime: len(ime)))
print(sorted(imena, key=lambda ime: ime[1]))
print(sorted(imena, key=lambda ime: ime[len(ime) - 1]))

#kriterij za urejanje nizov po dolžini in abecedi

def kriterij(niz):
    return(len(niz), niz)

# z lambdo, brez potrebe po ločeni definiciji funkcije print(sorted(imena, key=lambda ime: (len(ime), ime)))
print(sorted(imena, key=kriterij))


#tabelo t uredimo po absolutni vrednosti
t.sort(key=lambda stevilo: abs(stevilo))
print(t)