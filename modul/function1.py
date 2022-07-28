def harian (jam,tipe) :
    c = 0
    if tipe == 'mobil' :
        c = 2000 * jam
    elif tipe == 'motor' :
        c = 1000 * jam
    else :
        c = 0
    return c
    

