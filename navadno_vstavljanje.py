

def uredi(tabela):
    dolzina = len(tabela)
    
    for i in range(1, dolzina):

        # vstavi element tabela[i] na ustrezno mesto med elemente tabela[0], tabela[1], ... tabela [i]
        print(f'tabela prej: {tabela}')

        #element, ki ga vstavljamo na ustrezno mesto v levem (urejenem delu
        
        trenutni = tabela[i]

        j = i - 1
        while j >= 0 and tabela[j] > trenutni:
            tabela[j + 1] = tabela[j]

            j -= 1                    #j = j -1 (krajši zapis)

        tabela[j + 1] = trenutni

        print(f'tabela potem: {tabela}')
        print()

t = [70, 50, 100, 30, 90, 10, 60, 20, 80, 40]
uredi(t)
print(t)
