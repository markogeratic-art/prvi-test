
class Cas:
    def __init__(self, h, m):
        self.ura = h
        self.minuta = m

    def izpisi(self):
        print(f'{self.ura}:{self.minuta:02}')

    #
    # Vrne nov objekt tipa Cas, ki predstavlja trenutek, ki ga dobimo tako, da
    # podanemu času (self) prištejemo podani prištevek v minutah.
    #
    def __add__(self, pristevek):
        self_v_minutah = 60 * self.ura + self.minuta
        novi_v_minutah = (self_v_minutah + pristevek) % 1440
        nova_ura = novi_v_minutah // 60
        nova_minuta = novi_v_minutah % 60
        return Cas(nova_ura, nova_minuta)

    #
    # Vrne razliko med časoma self in drugi (v minutah).
    #
    def __sub__(self, drugi):
        if type(drugi).__name__ == 'int':
            # (demonstracija, ki ni konsistentna z zgornjim komentarjem)
            # vrnemo nov čas, ki je za <drugi> minut pred časom self
            return self + (-drugi)   # self.__add__(-drugi)

        self_v_minutah = 60 * self.ura + self.minuta
        drugi_v_minutah = 60 * drugi.ura + drugi.minuta
        return self_v_minutah - drugi_v_minutah

    #
    # Vrne true natanko v primeru, če je čas <self> kronološko manjši od časa
    # <drugi>.
    #
    def __lt__(self, drugi):
        '''
        if self.razlika(drugi) < 0:
            return True
        else:
            return False
        '''
        return self - drugi < 0

    #
    # Vrne true natanko v primeru, če je čas <self> kronološko manjši od časa
    # <drugi> ali enak času <drugi>.
    #
    def __le__(self, drugi):
        return self - drugi <= 0

    #
    # Ta funkcija se posredno pokliče, ko kličemo print(nek objekt tipa Cas)
    #
    def __str__(self):
        return f'{self.ura}:{self.minuta:02}'

if __name__ == '__main__':
    zajtrk = Cas(6, 50)
    kosilo = Cas(12, 30)
    vecerja = Cas(18, 40)

    malica = kosilo + 180    # to se izvede kot malica = kosilo.__add__(180)
    print(malica)    # 15:30

    print(vecerja - kosilo)   # 370
    print(zajtrk - kosilo)   # -340

    print(zajtrk < kosilo)    # True
    print(vecerja < kosilo)   # False
    print(kosilo < kosilo)    # False
    print(kosilo <= kosilo)   # True
    print(kosilo <= vecerja)  # True
    print(vecerja <= kosilo)  # False

    #print(kosilo - 50)    # kosilo.__sub__(50)
    #print(kosilo + Cas(10, 20))

    print(kosilo + (-50))    # kosilo.__add__(-50)
    print(kosilo - 50)    # kosilo.__sub__(50)

    print(kosilo - zajtrk) # 340

