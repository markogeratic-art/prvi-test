class PostniNaslov:
    def __init__(self, uh, ps, po):
        self.ulica_hs = uh
        self.postna_stevilka = ps
        self.posta = po

naslov_FE = PostniNaslov('Tržaska cesta 25', 1000, 'Ljubljana')
tetin_naslov = PostniNaslov('Mariborska 200', 3000, 'Celje')
mojcin_naslov = PostniNaslov('Gorenjska 3b', 4000, 'Kranj')

print(tetin_naslov.postna_stevilka)
print(naslov_FE.ulica_hs)

class Oseba:
    def __init__(self, im, priim, letoroj, naslov):
        self.ime = im
        self.priimek = priim
        self.leto_rojstva = letoroj
        self.postni_naslov = naslov

janez = Oseba('Janez', 'Novak', '1970', PostniNaslov('Celovška 150a', 1000, 'Ljubljana'))
teta = Oseba('Marija', 'Brodnik', 1950, tetin_naslov)
mojca = Oseba('Mojca', 'Bizjak', 1990, mojcin_naslov)
stric = Oseba('Ivan', 'Brodnik', 1948, tetin_naslov)
              
print(janez.priimek)
print(mojca.leto_rojstva)
print(teta.priimek == stric.priimek)
print(teta.postni_naslov.posta)
print(janez.postni_naslov.ulica_hs)