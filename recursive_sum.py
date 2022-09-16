

def sum(list):
    '''
    Returns the sum of all elements in a list
    '''

    #Base caes
    if not list:
        return 0

    #recursive case
    return list[0] + sum(list[1:])

my_list = [1, 3, 5, 7, 9]
print(sum(my_list))