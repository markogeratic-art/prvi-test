file_name = "kosovel.txt"

abeceda = "ABCČDEFGHIJKLMNOPRSŠTUVZŽ"

abeceda_slovar = dict(zip(abeceda, [0]*len(abeceda)))



with open(file_name, "r") as file:
    for line in file:
        for c in line.strip():
            if c in abeceda:
                abeceda_slovar[c] += 1

print(abeceda_slovar)