

def quicksort(list):
    '''
    
    '''

    #base case
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        left_half = [i for i in list[1:] if i <= pivot]
        right_half = [i for i in list[1:] if i > pivot]

        return quicksort(left_half) + [pivot] + quicksort(right_half)
    
      


my_list = [1, 3, 5, 7, 9]
print(quicksort(my_list))