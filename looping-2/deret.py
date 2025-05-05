# for x in range(1,20,2):
#     print(x,end=" ")

# 2 4 6 8 10 12 14 16
# 30 27 24 21 18 15 12 9
# 1 1 2 4 7 11 16 22 29


# result = 30
# add = 1

# for i in range(8) :
#     print(result, end=" ")
#     result -= add
#     add +=2

# 30 29 26 21 14 5 -6 -19

# 1 1 2 3 5 8 13 21 34 
a = b = c = 1
for i in range(9):
    print(c, end=" ")
    if (i >=1) :
        c = a+b
    a = b
    b = c

print("\n================\n")

a , b = 1 , 1 
for i in range(9):
    print(a, end=" ")
    a, b = b, a+b 

    
    

