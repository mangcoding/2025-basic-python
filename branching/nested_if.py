price = int(input("Enter vehicle price :"))
age = int(input("Enter vehicle age :"))
type = input("Enter vehicle type (car or motorcycle) :")
emission = tax = 0

if (type == "car"):
    emission = int(input("Enter Carbon Emission :"))

if (age <=5) :
    if (type == "car" and emission <=100) :
        tax = price*1/100
    elif (type == "car" and emission >100) :
        tax = price*2/100
    else:
        tax = price*0.5/100

elif (age >5 and age <=10) :
    if (type == "car" and emission <=100) :
        tax = price*2/100
    elif (type == "car" and emission >100) :
        tax = price*3/100
    else:
        tax = price*1/100
else:
    if type == "car" :
        tax = price*5/100
    else:
        tax = price*3/100

print("Your tax is",tax)