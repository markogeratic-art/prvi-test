#
# Izpiše vsa števila od sp_meja do vključno zg_meja.
#

def zaporedje_stevil(sp_meja, zg_meja):
    for i in range(sp_meja, zg_meja + 1):
        print(i)

#zaporedje(10, 20)

#
# Izpiše vse znake od sp:meja do vklučno zg_meja.
#

def zaporedje_znakov(sp_meja, zg_meja):
    for koda in range(ord(sp_meja), ord(zg_meja) + 1):
        print(chr(koda))


#zaporedje_znakov('G', 'L')

#
# Izpiše vse besede dolžine 2, sestavljene iz znakov od sp_meja do vklkjučno zg_meja
#

def zaporedje_besed_dolzine_2(sp_meja, zg_meja):
    for prvi in range(ord(sp_meja), ord(zg_meja) + 1):
        for drugi in range(ord(sp_meja), ord(zg_meja) + 1):
            prvi_znak = chr(prvi)
            drugi_znak = chr(drugi)
            #print(f'prvi_znak: {prvi_znak}, drugi: {drugi_znak}')
            beseda = prvi_znak + drugi_znak
            print(beseda)


zaporedje_besed_dolzine_2('G', 'L')

#
# Izpiše vse besede dolžine 2, sestavljene iz znakov od sp_meja do vklkjučno zg_meja
#

def zaporedje_besed_dolzine_3(sp_meja, zg_meja):
    for prvi in range(ord(sp_meja), ord(zg_meja) + 1):
        for drugi in range(ord(sp_meja), ord(zg_meja) + 1):
            for tretji in range(ord(sp_meja), ord(zg_meja) +1):
                prvi_znak = chr(prvi)
                drugi_znak = chr(drugi)
                tretji_znak = chr(tretji)
            #print(f'prvi_znak: {prvi_znak}, drugi: {drugi_znak}')
                beseda = prvi_znak + drugi_znak + tretji_znak
                print(beseda)
zaporedje_besed_dolzine_3('G', 'L')