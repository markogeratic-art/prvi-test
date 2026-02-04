def indeks_minimuma(tabela):
    naj_vrednost = tabela[0]
    naj_index = 0

    for i in range(len(tabela)):
        if tabela[i] < naj_vrednost:
            naj_vrednost = tabela[i]
            naj_index = i

    return naj_index

def index_minimuma_alt(tabela):
    naj_index = 0
    for i in range(1, len(tabela)):
        if tabela[i] < tabela[naj_index]:
            naj_index = i

    return naj_indeks






t = [40, 20, 30, 25, 55, 45, 35, 60, 15, 50]
print(indeks_minimuma(t))
