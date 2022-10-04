def cutTheSticks(arr):
    # Write your code here
    sticks_cut = []
    while arr:
        sticks_cut.append(len(arr))
        min_val = min(arr)
        count_min = arr.count(min_val)
        for i in range(count_min):
            index = arr.index(min_val)
            arr.pop(index)
        for i in arr:
            i -= min_val
    
    return sticks_cut