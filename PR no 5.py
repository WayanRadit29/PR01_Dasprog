#Jadi kita diminta membuat sebuah program yang outputnya itu volume cairan untuk di infus dan mencari debit infus (rate) dalam satuan ml/jam

vtbi = float(input("Masukan Volume Cairan Yang Harus Di Infus :"))
menitt = float(input("Masukan waktu target : "))

rate = vtbi/(menitt/60)
print("VTBI :", vtbi, "ml")
print("Rate :", rate, "ml/hr")