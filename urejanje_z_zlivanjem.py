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


#
# Uredi tabelo <tabela>
#

def uredi(tabela):
    dolzina = len(tabela)
    # tabela dolzine 0 ali 1 je že urejena

    if dolzina >= 2:
        # razbij tabelo na dva približno enaka dela
        prva = tabela[: dolzina // 2]
        druga = tabela[dolzina // 2 :]

        # uredi vsak del posebej
        uredi(prva)
        uredi(druga)

        #zlij urejeni podtabeli
        zlita = zlij(prva, druga)

        #rezultat zlivanja (= urejena kopija vhodne tabele() prepiši v vhodno tabelo
        tabela[:] = zlita

t = [20, 11, 17, 37, 42, 15, 27, 21, 33, 24]
uredi(t)
print(t)