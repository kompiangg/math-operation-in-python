print("Aplikasi untuk menghitung hasil faktorial")

angka = int(input("Masukkan angka yang diinginkan : "))
hasil = 1

while angka > 1:
    hasil *= angka * (angka-1)
    angka-=2

print("Hasilnya adalah :", hasil)