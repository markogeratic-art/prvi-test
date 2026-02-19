class Student:
    def __init__(self, vp, im, pr):
        self.vpisna_stevilka = vp
        self.ime =im
        self.priimek = pr
        self.tocke = []


    def __str__(self):
        vsota_tock = sum(self.tocke)
        """
        str_tocke = []
        for t in self.tocke:
            str_tocke.append(str(t))
            """
        #str_tocke = [str(t) for t in self.tocke] #krajša različica zgornje kode
        str_tocke = [f'{t:2}' for t in self.tocke]
        izpis_tock = ' '.join(str_tocke)
        return f'{self.vpisna_stevilka} {self.ime:<8} {self.priimek:<8} {izpis_tock} {vsota_tock:3}'
    

        
  #  def __repr__(self):
    #     return f'{self.ime} {self.priimek} ({self.vpisna_stevilka})'


#slovar, ki vpisno številko (niz) preslika v študenta (objekt tipa Student)

vpisna2student = {}

datoteka_vsi = open('/Users/markogeratic/Documents/Programi/prvi-test/OOP/vsi.csv')

for vrstica in datoteka_vsi:
    polja = vrstica.strip().split(';')
    vpisna_stevilka = polja[0]
    ime = polja[1]
    priimek = polja[2]
    #print(f'vpisna = <{vpisna_stevilka}>, ime = <{ime}>, priimek = <{priimek}>')
    student = Student(vpisna_stevilka, ime, priimek)
    #print(student)
    vpisna2student[vpisna_stevilka] = student

datoteka_vsi.close()
#print(studentje)

udelezenci_izpita = []

datoteka_izpit = open('/Users/markogeratic/Documents/Programi/prvi-test/OOP/izpit.csv')

for vrstica in datoteka_izpit:
    polja = vrstica.strip().split(';')
    vpisna_stevilka = polja[0]

    #pridobimo studenta, ki pripada pravkar prebrani vpisni številki
    student = vpisna2student[vpisna_stevilka]

    for i in range(1, len(polja)):
        student.tocke.append(int(polja[i]))

    udelezenci_izpita.append(student)
    #print(student)

datoteka_izpit.close()

#izpiši podatke o posameznih udeležencih izpita

"""
def kljuc_za_urejanje(student):
    return (sum(student.tocke), student.priimek, student.ime, student.vpisna_stevilka)
"""

udelezenci_izpita.sort(key=lambda student:
    (sum(student.tocke), student.priimek, student.ime, student.vpisna_stevilka))

#udelezenci_izpita.sort(key=kljuc_za_urejanje)

for student in udelezenci_izpita:
    print(student)