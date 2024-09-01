#Program untuk mencari kemungkinan nilai-nilai tripel phytagoras
import math

m = float(input("Masukan nilai m :"))
n = float(input("Masukan nilai n :"))

def tripel_phytagoras(m, n):
    if m > n:
        side1 = math.pow(m, 2) - math.pow(n, 2)
        side2 = 2 * m * n 
        hypotenusa = math.pow(m, 2) + math.pow(n, 2)
        print("Tripel Phytagoras : " ,side1, "," ,side2, ",",hypotenusa)
    else:
        return

tripel_phytagoras(m, n)