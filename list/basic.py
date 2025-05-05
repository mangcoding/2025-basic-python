list1 = [1,2,3.4, False, True, {"name":"Nugraha","birthdate":"2025-10-01"}]

print(list1[5])

number = [1,2,10,100]
newnumber = [x * 5 for x in number]
print(newnumber)

def multiple_by_5(n):
    return n*10

newnumberx = list(map(multiple_by_5,number))
print(newnumberx)
