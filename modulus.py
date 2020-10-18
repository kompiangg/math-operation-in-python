print("Perhatikan bentuk berikut")
print("-" * 19)
print("| a mod b = hasil |")
print("-" * 19)

a = int(input("Masukkan a : "))
b = int(input("Masukkan b : "))

if (a > 0 and b > 0) or (a < 0 and b < 0):
    hasil = a - int(a/b) * b
elif (a == 0 and b >= 0):
    hasil = 0
elif a > 0 and b == 0:
    hasil = a
elif a < 0 and b > 0:
    hasil = ((int(a/b - 1)) * -b) + a

print("hasilnya : ", hasil)
