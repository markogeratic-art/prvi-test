#
# Zljie naraščujoči tabeli a in b v novo tabelo in jo vrne.
#


def zlij(a, b):
    rezultat = []
    i = 0   # index za tabelo a
    j = 0   # index za tabelo b

    #prva faza: oba indeksa sta znotraj meja tabel

    dolzina_a = len(a)
    dolzina_b = len(b)

    while i < dolzina_a and j < dolzina_b:
        if a[i] < b[j]:
            rezultat.append(a[i])
            i += 1
        else:
            rezultat.append(b[j])
            j += 1

#   na tej točki velja bodisi i == dolzina_a bodisi j == dolzina_b
#   druga faza: v izhodno tabelo prepišemo preostale elemente tabele a oz. b

    while i < dolzina_a:            # ta zanka se bo izvedla samo v primeru, če je i < dolzina_a
        rezultat.append(a[i])
        i += 1

    while j < dolzina_b:            # ta zanka se bo izvedla samo v primeru, če je j < dolzina_b
        rezultat.append(b[j])
        j += 1

    return rezultat

prva = [7, 11, 13, 19, 20, 25, 30]
druga = [5, 9, 17, 24, 32, 37]

tretja = zlij(prva, druga)
print(tretja)
