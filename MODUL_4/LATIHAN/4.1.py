##def cariLurus( wadah, target) :
##    n = len(wadah)
##    for i in range(n):
##        if wadah[i] == target:
##            return True
##    return False
##class Manusia(object):
##    """Class manusia dengan inisiasi 'nama'"""
##    keadaan='lapar'
##    def __init__(self,nama):
##        self.nama = nama
##    def ucapSalam(self):
##        print("halo namaku: ", self.nama)
##    def makan(self,s):
##        print("saya baru saja makan ", s)
##        self.keadaan = 'kenyang'
##    def olah(self,k):
##        print('saya baru saja latihan', k)
##        self.keadaan='lapar'
##    def kali(self,n):
##        return n*2
##class mahasiswa(Manusia):
##    """Class Mahasiswa yang dibangun dai class Manusia"""
##    def __init__(self,nama,NIM,kota,us):
##        self.nama=nama
##        self.NIM=NIM
##        self.kotaTinggal=kota
##        self.uang=us
##    def __str__(self):
##        s=self.nama+',NIM '+str(self.NIM)\
##           +'. tinggal di '+self.kotaTinggal\
##           +'. uang saku Rp '+str(self.uang)\
##           +'. tiap bulan'
##        return s
##class MhsTIF(mahasiswa):
##     def __init__(self,nama,NIM,kota,us):
##        self.nama=nama
##        self.NIM=NIM
##        self.kotaTinggal=kota
##        self.uang=us
##     def __str__(self):
##        s=self.nama+',NIM '+str(self.NIM)\
##           +'. tinggal di '+self.kotaTinggal\
##           +'. uang saku Rp '+str(self.uang)\
##           +'. tiap bulan'
##        return s
##c0 = MhsTIF('Ika',10,'Sukoharjo',240000)
##c1 = MhsTIF('Budi',51,'Sragen',230000)
##c2 = MhsTIF('Ahmad',2,'Surakarta',250000)
##c3 = MhsTIF('Chandra',18,'Surakarta',235000)
##c4 = MhsTIF('Eka',4,'Boyolali',240000)
##c5 = MhsTIF('Fandi',31,'Salatiga',250000)
##c6 = MhsTIF('Deni',13,'Klaten',245000)
##c7 = MhsTIF('Galuh',5,'Wonogiri',245000)
##c8 = MhsTIF('Janto',23,'Klaten',245000)
##c9 = MhsTIF('Hasan',64,'Karanganyar',270000)
##c10 = MhsTIF('Khalid',29,'Purwodadi',265000)
##
##Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
##target = 'Klaten'
##for i in Daftar:
##    if i.kotaTinggal == target:
##        print(i.nama + 'tinggal di' + target)
##
def cariTerkecil( kumpulan ):
    n = len(kumpulan)
    terkecil = kumpulan[0]
    for i in range(1,n):
        if kumpulan[i] < terkecil:
            terkecil = kumpulan[i]
    return terkecil
    
