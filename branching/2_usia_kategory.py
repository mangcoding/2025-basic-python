usia = float(input("Masukkan usia : (dalam tahun)"))

if usia <=2 :
    category = "Bayi"
elif usia >2 and usia <=5 :
    category = "Balita"
elif usia >5 and usia <=12 :
    category = "Anak-anak"
elif usia >12 and usia <=18 :
    category = "Remaja"
else:
    category = "Dewasa"

print("Usia anda %s, termasuk dalam kategory %s"%(usia,category))
