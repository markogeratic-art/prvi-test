#
# Vrne število deliteljev danega števila
#

def stevilo_deliteljev(stevilo):
    stevec = 0
    for kandidat in range(1, stevilo + 1):
        if stevilo % kandidat == 0:
            #print(kandidat)
            stevec += 1
    return stevec





# grša rešitev
"""
n = int(input('Vnesi število : '))
poskus = 1

while True:
    if stevilo_deliteljev(poskus) >= n:
        break
    poskus += 1

print(poskus)
"""


#lepša rešitev

n = int(input("Vnesi število : "))
poskus = 1
while stevilo_deliteljev(poskus) < n:
    poskus += 1
print(poskus)