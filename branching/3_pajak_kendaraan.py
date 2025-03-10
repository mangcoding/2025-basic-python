category = input("Jenis Kendaraaan (mobil/motor) :")
value = int(input("Berapa nilai NJKB :"))
firstVehicle = input("Apakah ini kendaraan pertama? (ya/tidak):")
pkb = 2/100*value
final = 0

if (firstVehicle == "tidak") :
    numberVehicle = int(input("Kendaraan keberapa ini (2-20) :"))
    pkb = (2 + (numberVehicle - 1) * 0.5)/ 100 * value

if (category == "mobil") :
    final = pkb + 143000
else:
    final = pkb + 35000

print("Pajak Kendaraan Anda adalah %.2f"%final)


