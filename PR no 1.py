#Disini saya mencoba membuat program menghitung biaya total yang dibayar saat naik taksi


odometer1 = float(input("Masukan Nilai Odometer Awal :"))
odometer2 = float(input("Masukan Nilai Odometer Akhir :"))

distance = abs(odometer2 - odometer1) #Fungsi untuk nilai mutlak
fare = distance * 1.50
print("Jadi Kamu Telah Berkendara Sejauh : ", round(distance, 1), "miles Dan Kamu Harus Membayar : $", round(fare, 1))
