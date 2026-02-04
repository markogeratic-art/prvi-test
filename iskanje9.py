#
# PRVA VERZIJA - ISKANJE, KI UPOŠTEVA UREJENOST TABELE
# 
# 
# 
# 
# Če element <iščemo> obstaja v tabeli <tabela> vrne njegov indeks,
# sicer pa vrne -1. Predpostavimo, da je tabela naraščajoče urejena
#

import random
import time

def poisci_urejeno(tabela, iscemo):
    for index in range(len(tabela)):
        if tabela[index] == iscemo:
            return index
        if tabela[index] > iscemo:
            return -1
        
    return -1

#
#DRUGA VERZIJA ISKANJE BREZ UPOŠTEVANJA UREJENOSTI TABELE
#
#
# Vrne tabelo indeksov vseh pojavitev števila <iscemo> v tabeli <tabela>.
# (Če se iskano število v tabeli ne nahaja, naj potem vrne [])
#


def poisci_splosno(tabela, iscemo):
    indexi_pojavitev = []
    for index in range(len(tabela)):
        if tabela[index] == iscemo:
            indexi_pojavitev.append(index)
    return indexi_pojavitev

#
# Tretja verzija - bisekcijo
#

def poisci_dvojisko(tabela, iscemo):
    #indeks leve in desne meje relevantnega dela tabele (dela tabele, kjer se
    #lahko nahaja iskani element)
    l = 0
    d = len(tabela) -1

    while l <= d:
        # indeks sredinskega elementa v relevantenm delu tabele
        s = (l + d) // 2

        if tabela[s] == iscemo:
            return s
        
        if tabela[s] < iscemo:
            l = s + 1
        else:
            d = s - 1
        
    return -1


#zgradimo tabelo t = [2, 4, 6, ..., 200000]
t = []
stevilo = 10
for i in range(100000):
    t.append(stevilo)
    stevilo += 10

zacetek = time.time()   
for i in range(1000):
    poisci_splosno(t, random.randint(-1000, 1001000))
konec = time.time()
print(konec - zacetek)

zacetek = time.time()   
for i in range(1000):
    poisci_urejeno(t, random.randint(-1000, 1001000))
konec = time.time()
print(konec - zacetek)

zacetek = time.time()   
for i in range(1000):
    poisci_dvojisko(t, random.randint(-1000, 1001000))
konec = time.time()
print(konec - zacetek)