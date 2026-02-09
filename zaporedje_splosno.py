
def zaporedje_rek(ciljna_dolzina, zac_znak, kon_znak, tabela, nivo):
    #na i- tem nivoju rekurzije napolnemo i-to celico tabelo na vse možne načine

    #iztek rekurzije: tabelo napolnimo do konca
    if nivo == ciljna_dolzina:
        #print(tabela)
        niz = ''.join(tabela)
        print(niz)


    else:    
        for koda in range(ord(zac_znak), ord(kon_znak) + 1):
            znak = chr(koda)
            tabela[nivo] = znak
            zaporedje_rek(ciljna_dolzina, zac_znak, kon_znak, tabela, nivo + 1)


#
# Izpiše vse nize podane dolžine, sestavljene iz znakov od zac_znak do kon_znak.
#


def zaporedje(dolzina, zac_znak, kon_znak):
    # tabela, ki jo bomo polnili z znaki
    tabela = [' ' * dolzina]
    zaporedje_rek(dolzina, zac_znak, kon_znak, tabela, 0)


zaporedje(4, 'A', 'C')