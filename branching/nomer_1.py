is_bayar = input("Apakah sudah bayar Semester? (ya/tidak): ")
nilai_d = input("Apakah anda memiliki nilai D? (ya/tidak): ")

if (is_bayar == 'ya' and nilai_d == 'tidak') :
    print("Selamat anda lulus")
else :
    print("Maaf anda tidak lulus")