from hashlib import new


new_list = [1, 2, 4,]
result = new_list[0] #constant time operetion

if 1 in new_list: print(True) #in calls a contains method defined for list type which does a linear search


for n in new_list: #Linear search
    if n == 1:
        print(True)

        break