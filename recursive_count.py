def count(list):
    """
    Returns number of items in a list
    """

    # base case
    if not list:
        return 0

    # recursive case
    return 1 + count(list[1:])


my_list = [1, 3, 5, 7, 9]
print(count(my_list))
