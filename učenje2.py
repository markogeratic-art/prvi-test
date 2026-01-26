teza = float(input(85))
visina = float(input(182))
bmi = teza / visina ** 2
print("Indeks vaše telesne teže je", bmi)
if bmi > 25:
    print("potrebno bo shujšati)")
else:
    print("odlično, le pe naprej jejte toliko kot doslej!")