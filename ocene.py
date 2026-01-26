studenti = {'Maja': 5, 'Eva': 2, 'Borut': 4, 'Simon': 1}
            
pozitivni = []
negativni = []

for s in studenti:   #s pomeni vsak element v tej množici
    if studenti[s] > 1:
        pozitivni.append(s)
    else:
        negativni.append(s)
    

print("+:", pozitivni, "-:", negativni)