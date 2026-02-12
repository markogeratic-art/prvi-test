def izstevanka(imena, st_besed):

    st_otrok = len(imena)
    st_krogov = st_otrok - 1

    for krog in range(st_otrok - 1):

        # ugotovi kdo izpade
        index_izpadlega = (st_besed -1) % st_otrok

        # izloči izpadlega

        print(imena[index_izpadlega])

        #del imena[index_izpadlega] - običajen način
    
        for i in range(index_izpadlega, st_otrok - 1):
            imena[i] = imena[i +1]

        st_otrok -= 1

izstevanka(['Ana', 'Bojan', 'Cvetka', 'Denis', 'Eva'], 9)
