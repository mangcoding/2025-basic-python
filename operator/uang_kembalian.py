uang_1000 = uang_500 = 0
uang = 17500

sisa_uang_1000 = uang % 1000
uang_1000 = (uang - sisa_uang_1000) / 1000
print(f"Uang 1000 = {int(uang_1000)} lembar")

sisa_uang_500 = sisa_uang_1000 % 500
uang_500 = (sisa_uang_1000 - sisa_uang_500) / 500
print(f"Uang 500 = {int(uang_500)} keping")