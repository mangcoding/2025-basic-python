nilai=int(input("Masukkan nilai: "))
grade='E'

if nilai >=85:
    grade = 'A'
elif nilai >=75:
    grade = 'B'
elif nilai >=65:
    grade = 'C'
elif nilai >=55:
    grade = 'D'

print("Grade anda adalah %s"%grade)