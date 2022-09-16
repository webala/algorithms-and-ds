

def selection_sort(list):
    sorted_list = []
    
    while list:
        lowest = list[0]
        index = 0
        for i in range(len(list)):
            if list[i] < lowest:
                lowest = list[i]
                index = i
        sorted_list.append(list.pop(index))
    return sorted_list

my_list = [5,3,8,7,9,20]
print(selection_sort(my_list))