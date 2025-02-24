a = 0
b = 0
c = 0

for x in range(10):
    if x < 1:
        result = 0
    elif (x == 1) :
        result = 1
    elif (x == 2) :
        result = 1
    else :
        result = a + b + c  
    print(result, end=" ")
    a = b
    b = c
    c = result 