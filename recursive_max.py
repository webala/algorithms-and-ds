

def max(list):
    '''
    Returns the maximum number in a list
    '''
    if len(list) == 1:
        return list[0]
    mid = len(list) // 2
    left_half = list[:mid]
    right_half = list[mid:]

    left = max(left_half)
    right = max(right_half)

    if left > right:
        return left
    else:
        return right

my_list = [1, 3, 5, 7, 9, 11]
print(max(my_list))

