#Program yang menghitung lama waktu memotong rumput pada sebuah halaman (persegi panjang) yang terdapat sebuah rumah(persegi panjang) di halaman tersebut dan diketahui kecepatan memotongnya 2 kaki persegi per detik

print("User harus menginput nilai panjang dan lebar dari halaman dan rumah dalam satuan kaki persegi")
phalaman = float(input("Masukan Panjang Halaman : "))
lhalaman = float(input("Masukan Lebar Halaman : "))
prumah = float(input("Masukan Panjang Rumah : "))
lrumah = float(input("Masukan Lebar Rumah : "))

#Program mulai menghitung waktu yang diperlukan untuk memotong rumputnya, jika kecepatannya 2 kaki persegi per detik
if phalaman < lhalaman and prumah > lrumah:
    luas_halaman = phalaman * lhalaman
    luas_rumah = phalaman * lrumah
    if luas_halaman > luas_rumah:
        luas_rumput = luas_halaman - luas_rumah
        t_potong = luas_rumput / 2
        print("Jadi waktu untuk memotong rumput itu :", t_potong, "detik")
    else:
        print("Maaf konteksnya disini luas halaman lebih dari luas rumah karena di soal menyatakan sebuah rumah terletak di sebuah halaman dan bukan sebuah halaman yang terletak di sebuah rumah")
elif phalaman > lhalaman and prumah < lrumah:
    luas_halaman = phalaman * lhalaman
    luas_rumah = prumah * lhalaman
    if luas_halaman > luas_rumah:
        luas_rumput =  luas_halaman - luas_rumah
        t_potong = luas_rumput / 2
        print("Jadi waktu untuk memotong rumput itu :", t_potong, "detik")
    else:
        print("Maaf konteksnya disini luas halaman lebih dari luas rumah karena di soal menyatakan sebuah rumah terletak di sebuah halaman dan bukan sebuah halaman yang terletak di sebuah rumah")
else: 
    luas_halaman = phalaman * lhalaman
    luas_rumah = prumah * lrumah
    if luas_halaman > luas_rumah:
        luas_rumput = luas_halaman - luas_rumah
        t_potong = luas_rumput / 2 
        print("Jadi waktu untuk memotong rumput itu :", t_potong, "detik")
    else:
        print("Maaf konteksnya disini luas halaman lebih dari luas rumah karena di soal menyatakan sebuah rumah terletak di sebuah halaman dan bukan sebuah halaman yang terletak di sebuah rumah")
    

