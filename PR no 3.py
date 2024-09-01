#Program yang akan mengestimasikan suhu sejak mati listrik di freezer

tjam = float(input("Masukan Durasi dalam Jam : "))
tmenit = float(input("Masukan Durasi Tambahan dalam Menit (Jika Ada) : "))

takhir = tjam + tmenit/60

Temperature_freezer = ((4 * (takhir ** 2)) / (takhir + 2)) - 20
print("Suhu Freezer Sekarang : ", Temperature_freezer)

