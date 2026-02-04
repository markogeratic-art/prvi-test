import random
import time

def navadno_vstavljanje(tabela):
    dolzina = len(tabela)
    
    for i in range(1, dolzina):

        # vstavi element tabela[i] na ustrezno mesto med elemente tabela[0], tabela[1], ... tabela [i]
    

        #element, ki ga vstavljamo na ustrezno mesto v levem (urejenem delu
        
        trenutni = tabela[i]

        j = i - 1
        while j >= 0 and tabela[j] > trenutni:
            tabela[j + 1] = tabela[j]

            j -= 1                    #j = j -1 (krajši zapis)

        tabela[j + 1] = trenutni


def index_minimuma(tabela, index_zac, index_kon):

    naj_index = index_zac

    for i in range(index_zac +1, index_kon +1):
        if tabela[i] < tabela[naj_index]:
            naj_index = i

    return naj_index


def navadno_izbiranje(tabela):
    dolzina = len(tabela)
    for i in range(dolzina):
        # zamenjaj element tabela[i] z najmanjšim izmed elementov tabela[i], tabela[i +1],...., tabela [dolzina -1]

   

        # poišči indeks najmanjšega izmed elemntov tabela [i], ... , tabela[dolzina -1]
        imin = index_minimuma(tabela, i, dolzina - 1)
        

        #med seboj zamenjaj elementa tabela[imin] in tabela[i]
        
        pomozna = tabela[imin]
        tabela[imin] = tabela[i]
        tabela[i] = pomozna


def nakljucna_tabela(dolzina):
    tabela = []
    for i in range(dolzina):
        element = random.randint(1, 10 ** 6)
        tabela.append(element)
    return tabela

def urejena_tabela(dolzina):
    tabela = []
    for i in range(dolzina):
        tabela.append(i)
    return tabela
    
def obratno_urejena_tabela(dolzina):
    tabela = []
    for i in range(dolzina):
        tabela.append(dolzina - i - 1)
    return tabela

#osnova = nakljucna_tabela(10 ** 4)
#osnova = urejena_tabela(10 ** 4)
osnova = obratno_urejena_tabela(10 **4)


zacetek = time.time()
tabela = osnova[:]      #kopija tabele
navadno_izbiranje(tabela)
konec = time.time()
print(konec - zacetek)

tabela = osnova[:]
zacetek = time.time()
navadno_vstavljanje(tabela)
konec = time.time()
print(konec - zacetek)