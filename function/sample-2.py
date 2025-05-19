def HelloString(name) :
    print("Hallo", name, "Selamat Datang")

def HelloFromArray(names):
    for name in names :
        print("Hallo", name, "Selamat Datang")

names = ["Nurul","Lendis","Fabri","Isa"]

for name in names :
    HelloString(name)

HelloFromArray(names)