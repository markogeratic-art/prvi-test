class Student:
    def __init__(self, im, pr, sb):
        self.ime = im
        self.priimek = pr
        self.stroski_bivanja = sb

    def __str__(self):
        return f' {self.ime} {self.priimek}'
    
    def stroski(self):
        return self.stroski_bivanja

#
# Razred izredni student je dedič (podrazred) razreda student. To pomeni, da podeduje vse njegove aribute in funkcije
#



class IzredniStudent(Student):
    def __init__(self, im, pr, sb, sol):
        #self.ime = im
        #self.priimek = pr
        #self.stroski_bivanja = sb
        super().__init__(im, pr, sb) #klic funkcije __init__ v razredu Student
        self.solnina = sol


    def stroski(self):
        #return self.stroski_bivanja + self.solnina

        #stroški za izrednega študenta se izračunajo na enak način kot stroški za navadnega študenta, le da se jim prišteje še šolnina
        return super().stroski() + self.solnina
janez = Student('Janez', 'Novak', 500)
print(janez)
print(janez.stroski())

miha = IzredniStudent('Miha', 'Rupnik', 400, 700)
print(miha)
print(miha.stroski())