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


t = [-7, 6, 9, -3, -8, 4, -5, -2, -6, -4]

kvadrat = lambda x: x ** 2      #krajši zapis za def kvadrat: return x ** 2
print(kvadrat(4))


print(minimum(t, kvadrat))
print(minimum(t, lambda x: x ** 2))