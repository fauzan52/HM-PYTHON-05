a = [1,2,3,4,5,6,7]
index = input ("Mau menampilkan index ke - berapa ? ")

try : 
    indexint = int (index)
    print (a[indexint])    
except IndexError : 
    print ("Index terlalu besar, maksimal {}".format(len(a-1)))
finally :
    print ("Kode selanjutnya ...")