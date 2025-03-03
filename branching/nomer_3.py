x = input("Input x: ")
y = input("Input y: ")

x = bool(int(x) == 1)
y = bool(int(y) == 1)

print(x and y)
print(x or y)
print(not x)
print(not (x or y))