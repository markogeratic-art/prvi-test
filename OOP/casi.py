class Cas:
    def __init__(self, h, m):
        self.ura = h
        self.minuta = m

    def izpisi(self):
        print(f'{self.ura}:{self.minuta:02}')

#
# Vrne nov objekt tipa Cas, ki predsatavlja trenutek, ki ga dobimo tako, da podanemu času (self) prištejemo podani prištevek v minutah.
#


    def plus(self, pristevek):
        self_v_minutah = 60 * self.ura + self.minuta
        novi_v_minutah = (self_v_minutah + pristevek) % 1440
        nova_ura = novi_v_minutah // 60
        nova_minuta = novi_v_minutah % 60
        return Cas(nova_ura, nova_minuta)

    #
    # Vrne True natako v primru, če je čas <selgf> kronolosko manjsi od časa <drugi>
    #


    def je_manjsi_od(self, drugi):

        '''
        if self.razlike(drug) < 0:
            return True
        else:
            return False

        '''
        return self.razlika(drugi) < 0

    def je_manjsi_ali_enak_kot(self, drugi):
        return self.razlika(drugi) <= 0

    #
    # Vrne razliko med časoma self in drugi (V minutah)
    #

    def razlika(self, drugi):
         self_v_minutah = 60 * self.ura + self.minuta
         drugi_v_minutah = 60 * drugi.ura + drugi.minuta
         return self_v_minutah - drugi_v_minutah

    #
    # Ta se funkcija se posredno pokliče, ko kličemo print(nek objekt tipa Cas)
    #

    def __str__(self):
        return f'{self.ura}:{self.minuta:02}'


if __name__ = '__main__':

zajtrk = Cas(6, 50)
kosilo = Cas(12, 30)
vecerja = Cas(18, 40)
print(zajtrk.ura)
print(kosilo.minuta)

#print(zajtrk)

spat = Cas(22, 5)
spat.izpisi()
zajtrk.izpisi()

print(zajtrk)
print(spat)

sprehod = kosilo.plus(120)
print(sprehod)
print(kosilo)
print(spat.plus(120))
print()

print(kosilo.razlika(zajtrk))


if zajtrk.je_manjsi_od(kosilo):
    print('Zajtrk je pred kosilom')
else:
    print('Kosilo je pred zajtrkom')