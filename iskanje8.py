#
# PRepostavimo, da je tabela naraščujoče urejena.
# Funkcija uporablja dvojiško iskanje (bisekcijo)

def posici_dvojisko(tabela, iscemo):
    #indeks leve in desne meje relevantnega dela tabele (dela tabele, kjer se
    #lahko nahaja iskani element)
    l = 0
    d = len(tabela) -1

    while l <= d:
        # indeks sredinskega elementa v relevantenm delu tabele
        s = (l + d) // 2

        if tabela[s] == iscemo:
            return s
        
        if tabela[s] < iscemo:
            l = s + 1
        else:
            d = s - 1
        
    return -1

t = [12, 17, 20, 22, 24, 26, 29, 32, 37, 42, 50, 52, 61, 69, 75]
print(posici_dvojisko(t, 50))
print(posici_dvojisko(t, 12))
print(posici_dvojisko(t, 75))
print(posici_dvojisko(t, 22))
print(posici_dvojisko(t, 69))
print(posici_dvojisko(t, 49))
print(posici_dvojisko(t, 1))


testi = [50, 12, 75, 22, 69, 39, 1, 100, 56, 18]
for test in testi:
    print(posici_dvojisko(t, test))


