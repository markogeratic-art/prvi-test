#import casi
from casi import Cas

ura_zac = int(input('Vnesi uro začetka: '))
min_zac = int(input('Vnesi minuto začetka: '))
ura_kon = int(input('Vnesi uro konca: '))
min_kon = int(input('Vnesi minuto konca: '))
interval = int(input('Vnesi interval v minutah: '))
trenutni_cas = Cas(ura_zac, min_zac)
koncni_cas = Cas(ura_kon, min_kon)

while trenutni_cas.je_manjsi_ali_enak_kot(koncni_cas):
    print(trenutni_cas)
    trenutni_cas = trenutni_cas.plus(interval)
