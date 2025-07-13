#data yang dimasukan pasti string
data = input("Masukkan nama:  ")

print("data = ", data, ",type =", type(data))

#Jika kita ingin mengambil int, maka
angka = float(input("Masukkan angka:  "))
angka = int(input("Masukkan angka:  "))
print("data = ", angka, ",type =", type(angka))

#Jika kita ingin mengambil boolean, maka
binner = bool(int(input("Masukkan binner (0 atau 1):  ")))

print("data = ", binner, ",type =", type(binner))
