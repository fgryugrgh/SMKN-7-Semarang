suhu = int(input("Masukan suhu = "))

while True:

    satuan1 = input("Satuan suhu yang ingin di konversi (C, K, Re, F)= ")
    satuan1 = satuan1.upper()
    satuan2 = input("Konversikan ke satuan suhu (C, K, Re, F)= ")
    satuan2 = satuan2.upper()

    if satuan1 in ["C", "K", "RE", "F"] and satuan2 in ["C", "K", "RE", "F"]: 
        break
    else:
        print("satuan salah")
        continue

if satuan1 == "C":
    celsius = suhu
elif satuan1 == "K":
    celsius = suhu - 273.15
elif satuan1 == "RE":
    celsius = suhu * (5/4)
else:
    celsius = (suhu - 32) * (5/9)

if satuan2 == "C":
    hasil = celsius
    hasil = str(hasil) + "°C"
elif satuan2 == "K":
    hasil = celsius + 273.15
    hasil = str(hasil) + "K"
elif satuan2 == "RE":
    hasil = celsius * (4/5)
    hasil = str(hasil) + "°Ré"
else:
    hasil = celsius * (9/5) + 32
    hasil = str(hasil) + "°F"

print("Hasil konversi mu adalah " + str(hasil))
