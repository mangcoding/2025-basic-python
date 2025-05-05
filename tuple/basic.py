days = ("Sunday","Monday","Tuesday")
print(days[0])

list = [1,1,1,2,2,4]
sets = set(list)

print(list)
print(sets)

newset = {2,2,5,10,10,10}
set2 = {1,1,1,4,5}

combine_set = newset.union(set2)
intersect_set = newset.intersection(set2)
print(combine_set, intersect_set)