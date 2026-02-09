n = int(input('Vnesi n: '))

for vrstica in range(n):
    #izpiši vrstico z indeksom <vrstica>
    for stolpec in range(n):
        if (vrstica + stolpec) % 2 == 0:
            print('o', end = '')
        else:
            print('*', end = '')
    print()