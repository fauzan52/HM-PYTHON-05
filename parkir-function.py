# # import semua function
# from function1 import *

# # import salah satu function
# from function2 import langganan

# import semua function beda folder
import sys
sys.path.insert (0, 'C:/Users/USER/Documents/Fauzan Alghifari/HM-PYTHON-05/modul')
from function2 import *

golongan = input ('golongan parkir = (harian/langganan)')
tipe = input ('Masukkan tipe kendaraan = (mobil/motor)')
if golongan == 'harian' :
    jamparkir = input ('berapa lama parkir = ')
    biayawal = 3000
    lamaparkir = int(jamparkir)
    ongkos = harian (lamaparkir,tipe)
    if lamaparkir < 2 :
        print ('Total lama parkir anda adalah ', jamparkir, "jam")
        print ('Biaya parkir anda adalah Rp', biayawal)
    elif lamaparkir <10 :
        biayaselanjutnya = (lamaparkir-1) * 2000 + biayawal
        print ('Total lama parkir anda adalah ', jamparkir, "jam")
        print ('Biaya parkir anda adalah Rp', biayaselanjutnya)
    else :
        print ('Total lama parkir anda adalah ', jamparkir, "jam")
        print ('Biaya parkir anda adalah Rp', 20000)
    print ('Ongkos harian = {}'.format(ongkos))
    
elif golongan == 'langganan' :
    saldo = 50000
    saldoakhir = langganan(saldo)
    print ('Ongkos langganan = {}'.format(saldoakhir))