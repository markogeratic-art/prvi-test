#
#vrne true natanko v primeru, če se dami na poljih (vr_prve, st_prve) in (vr_druge, st_druge) med seboj napadata
#
import time


def se_napadata(vr_prve, st_prve, vr_druge, st_druge):
    if vr_prve == vr_druge:
        return True
    if st_prve == st_druge:
        return True
    if vr_prve + st_prve == vr_druge + st_druge:        #dami sta na isti naraščajoči diagonali
        return True
    if vr_prve - st_prve == vr_druge - st_druge:
        return True
    return False

#
# Vrne True natako v primeru, če vsaj ena dama napada polje (vrstica, stolpec)
# polozaji_dam[i]: indeks vrstice

def je_napadeno(polozaji_dam, vrstica, stolpec):
    for i in range(stolpec):
        st = i
        vr = polozaji_dam[i]
        if se_napadata(vrstica, stolpec, vr, st):
            return True
    return False





#print(se_napadata(6, 2, 3, 5))
#print(se_napadata(6, 2, 7, 4))

#
# polozaji_dam[i]: indeks vrstice, v kateri se nahaja i-ta dama (ta se nahaja v stolpcu i)
#


#
# Poskusi postaviti damo v podani stolpec, tako da se napada z nobeno od že postavljenih dam in nato rekurzivno napolni še ostale stolpce
#

def poisci(velikost, polozaji_dam, stolpec):
    if stolpec == velikost:
        print(polozaji_dam)
    else:
        for vrstica in range(velikost):
            # ali vsaj ena dama v taeli polozaji_dam napada polje(vrstica, stolpec)
            if not je_napadeno(polozaji_dam, vrstica, stolpec):
                polozaji_dam[stolpec] = vrstica
                poisci(velikost, polozaji_dam, stolpec + 1)


velikost = int(input('vnesi velikos šahovnice: '))
polozaji_dam = [-1] * velikost
poisci(velikost, polozaji_dam, 0)