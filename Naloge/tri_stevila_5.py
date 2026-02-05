#
# Napišite program, ki prebere tri števila in izpiše največje med njimi.
# 
# Primer:
#
# Vnesite prvo število: 6
# Vnesite drugo število: 8
# Vnesite tretje število: 5
# Največje število je 8
#
#

stevilo1 = int(input('Vnesi število 1:'))
stevilo2 = int(input('Vnesi število 2:'))
stevilo3 = int(input('Vnesi število 3:'))

najvecje = max(stevilo1, stevilo2, stevilo3)

print(f' Najvecje število je: {najvecje}')