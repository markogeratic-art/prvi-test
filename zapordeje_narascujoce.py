def zaporedje_rek(ciljna_dolzina, zac_znak, kon_znak, tabela, nivo):
    # Na i-tem nivoju rekurzije napolnimo i-to celico tabele na vse možne
    # načine.

    # Iztek rekurzije: tabelo napolnimo do konca 
    if nivo == ciljna_dolzina:
        #print(tabela)
        niz = ''.join(tabela)
        print(niz)

    else:
        if nivo == 0:
            sp_meja = ord(zac_znak)
        else:
            sp_meja = ord(tabela[nivo - 1]) + 1
        for koda in range(sp_meja, ord(kon_znak) + 1):
            znak = chr(koda)
            tabela[nivo] = znak
            zaporedje_rek(ciljna_dolzina, zac_znak, kon_znak, tabela, nivo + 1)

#
# Izpiše vse nize podane dolžine, sestavljene iz znakov od zac_znak do
# kon_znak.
#

def zaporedje(dolzina, zac_znak, kon_znak):
    # tabelo, ki jo bomo polnili z znaki
    tabela = [' '] * dolzina
    zaporedje_rek(dolzina, zac_znak, kon_znak, tabela, 0)

#zaporedje(4, 'A', 'C')
#zaporedje(3, 'G', 'L')
zaporedje(3, 'A', 'E')