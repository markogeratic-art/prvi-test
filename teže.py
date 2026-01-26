teze = [74, 82, 58, 66, 61, 84]
imena = ["anze", "benjamin", "cilka", "dani", "eva", "franc"]
for teza in teze:
    print(teza, teza **2)

for teza in teze:
    if teza > 70:
        print(teza)

najlazji = 1000
for teza in teze:
    if teza < najlazji:
        najlazji = teza
print(najlazji)

s = 0
for teza in teze:
    s += teza
s /= len(teze)
print(s)

ime = "Cika"
for crka in ime:
    print(crka)