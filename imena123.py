imena = ['Denis', 'Franci', 'Gabrijela', 'Andreja', 'Hana', 'Cvetka', 'Eva', 'Bojan']
print(min(imena))
print(max(imena))
print(minimum(imena, lambda ime: len(ime)))
print(min(imena, key=lambda ime: len(ime)))
print(min(imena, key=lambda ime: -len(ime)))

print(sorted(imena))
print(sorted(imena, key=lambda ime: len(ime)))
print(sorted(imena, key=lambda ime: ime[1]))