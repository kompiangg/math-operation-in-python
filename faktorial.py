def faktorial(angka):
    hasil = 1
    if angka > 0 :
        while angka > 1:
            hasil *= angka * (angka-1)
            angka-=2
        print("Hasilnya adalah :", hasil)
    elif angka == 0:
        hasil = 0
        print("Hasilnya adalah :", hasil)
    else:
        print("Angka harus bilangan cacah")

print("Aplikasi untuk menghitung hasil faktorial")
print("Perhatikan berntuk di bawah")
print("")
print("-" * 59)
print("| a! = 1 x 2 x ... x (a-1) x a,\
 a himpunan bilangan cacah |")
print("-" * 59)
print("")

angka = int(input("Masukkan angka yang diinginkan : "))

faktorial(angka)