from logging import exception
from multiprocessing.managers import ValueProxy


a = input ("Masukkan pembilang = ")
b = input ("Masukkan penyebut = ")

# Manipulasi error
try:
    aint = int (a)
    bint = int (b)
    if bint == 2 :
        # TIDAK BOLEH MEMASUKKAN ANGKA 2
        raise Exception
    if bint == 3 :
        # TIDAK BOLEH MEMASUKKAN ANGKA 3
        raise Exception
    c = aint / bint
except ZeroDivisionError :
    print ("Penyebut tidak boleh nol")
except ValueError :
    print ("Tolong masukkan angka ...")
except Exception:
    print ("Tidak boleh memasukkan angka 2 atau 3")
else:
    print ("Hasil bagi a/b adalah {} " .format(c))
finally :
    print ("Kode selanjutnya ...")