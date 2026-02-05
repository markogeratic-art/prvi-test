

def fibonacci(n, shramba):
    if n <= 1:
        return n
    
    if shramba[n] >= 0:
        #juhuhu, fibonacci(n) smo že izračunali
        return shramba[n]

    shramba[n] = fibonacci(n - 2, shramba) + fibonacci(n - 1, shramba)
    return shramba[n]


#tabela, ki hrani že izračunane rezultate funkcije <fibonacci>
# shramba[i]: -1, če fibonacci(i) še nismo izračunali;
#       fibonacci(i), če smo fibonacci(i) že izračunali.

n = int(input('Vnesi n: '))
shramba = [-1] * (n + 1)
print(fibonacci(n, shramba))