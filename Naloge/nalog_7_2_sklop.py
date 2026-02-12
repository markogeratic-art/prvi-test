def tabela_indexov_sodih(t):
    indexi_sodih = []
    for index in range(len(t)):
        if t[index] % 2 == 0:
            indexi_sodih.append(index)
    return indexi_sodih


#
# Vrne tabelo indeksov sodih elementov tabele <t> (alternativna rešitev)
#

def tabela_indexov_sodih_alt(t):
    return [index for index in range(len(t)) if t[index] % 2 == 0]


moja_tabela = [17, 11, 12, 18, 22, 23, 28, 10]
print(tabela_indexov_sodih(moja_tabela))
print(tabela_indexov_sodih_alt(moja_tabela))