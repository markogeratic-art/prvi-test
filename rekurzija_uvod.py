def prva(n):
    print(f'Prva: {n}')
    druga(n - 1)
    print(f'Prva: {n}')

def druga(n):
    print(f'Druga: {n}')

#print(5)



#
# n- krat izšpiše 'Dober dan!'
#


def izpis(n):
    for i in range(n):
        print('Dober dan!')

def izpis_rek(n):
    if n > 0:
        print('Dober dan!')
        izpis_rek(n - 1)
        #print('Adijo!')

#izpis(7)
#izpis_rek(4)





#
# Vrne vsoto števil od vključno a do vključno b.
# na pirmer: vsota(3, 7) = 3 +4 +5 +6 +7 = 25

def vsota(a, b):
    rezultat = 0
    for i in range(a, b + 1):
        rezultat += i
    return rezultat

print(vsota(3, 7))

def vsota_rek(a, b):
    if a > b:
        return 0
    if a == b:
        return a
    return a + vsota_rek(a +1, b)

print(vsota_rek(3, 7))
    