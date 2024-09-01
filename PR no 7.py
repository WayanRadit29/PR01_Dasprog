#Program untuk menghitung berapa BTU yang disalurkan kepada sebuah rumah berdasarkan data galon minyak yang sudah dibakar dan eficiency dari tungku 

#Diasumsikan 42 Galon minyak setara dengan 5.800.000 BTU
galon_minyak = int(input("Input Jumlah Galon Minyak :"))
efficiency = int(input("Input Efisiensi Tungku :"))
BTU_total = 5800000 / 42 * galon_minyak

#Menghitung BTU yang tersalur
BTU_tersalur = (efficiency * BTU_total) / 100
print("Jadi yang tersalur ke rumah : ", BTU_tersalur, "BTU")




