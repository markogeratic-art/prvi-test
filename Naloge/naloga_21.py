
n = int(input('Vnesi n:'))


for vrstica in range(1, n + 1):
    for stolpec in range(1, n + 1):
        #print(vrstica * stolpec, end = ' ')
        zmnozek = vrstica * stolpec
        print(f'{zmnozek:4}', end=' ')
    print()
