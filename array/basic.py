import numpy as np

students = np.array(["John", 1, False, "Jill"], dtype=str)
print(students[3])

students2 = ["John", 1, False, "Jill"]
print(students2[3])

number = [1,3,5,6,7]

def toString(n):
    return (n)

#sample mapping
output = map(toString,students2)
print(list(output))