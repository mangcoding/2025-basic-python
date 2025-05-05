import numpy as np

#list is mutable 
list = [1,2,4,10] 
list2 = list
list2.append(20)
print(list)

newlist = np.array([1,2,4,10],dtype=int)
newlist2 = newlist
np.append(newlist2,20)
print(newlist2)

