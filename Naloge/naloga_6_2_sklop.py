#
# Vrne tabelo sodih elementov tabele <t>
#

def tabela_sodih(t):
    sodi = []
    for element in t:
        if element % 2 == 0:
            sodi.append(element)
        return sodi
    
#
# Vrne tabelo sodih elementov tabele <t> (alternativna rešitev)
#
def tabela_sodih_alt(t):
    return [element for element in t if element % 2 == 0]

moja_tabela = [17, 11, 12, 18, 22, 23, 28, 10]
print(tabela_sodih(moja_tabela))
print(tabela_sodih_alt(moja_tabela))