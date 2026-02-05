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
        print('Adijo!')

#izpis(7)
izpis_rek(4)





#
# Vrne vsoto števil od 1 do n.
#
'''
def vsota(n):
'''