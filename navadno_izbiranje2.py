# ta funkcija vnre indeks najmanjšega elementa v podani tabeli

# vrne indeks najmanjšega elementa tabele med indeksoma indeks_zac in indeks_kon
#




def index_minimuma(tabela, index_zac, index_kon):

    naj_index = index_zac

    for i in range(index_zac +1, index_kon +1):
        if tabela[i] < tabela[naj_index]:
            naj_index = i

    return naj_index


def uredi(tabela):
    dolzina = len(tabela)
    for i in range(dolzina):
        # zamenjaj element tabela[i] z najmanjšim izmed elementov tabela[i], tabela[i +1],...., tabela [dolzina -1]

        print(f'tabela prej: {tabela}')

        # poišči indeks najmanjšega izmed elemntov tabela [i], ... , tabela[dolzina -1]
        imin = index_minimuma(tabela, i, dolzina - 1)
        print(f'i = {i}, imin = {min}, tabela = {tabela}')

        #med seboj zamenjaj elementa tabela[imin] in tabela[i]
        
        pomozna = tabela[imin]
        tabela[imin] = tabela[i]
        tabela[i] = pomozna



t = [70, 50, 100, 30, 90, 10, 60, 20, 80, 40]
uredi(t)
print(t)