#Program untuk memprediksi jumlah section dalam suatu batch dan jumlah siswa yang akan ditinggalkan, jika diberikan input jumlah total siswa

jumlah_siswa = int(input("Masukan Jumlah Total Siswa : "))
section = int(jumlah_siswa / 30)
sisa_siswa = jumlah_siswa - (section * 30)
print("Section : ", section)
print("Sisa Siswa : ", sisa_siswa)