def pickingNumbers(a):
    # Write your code here
    values = list(set(a))
    max_count = 0
    if len(values) == 1:
        max_count = a.count(values[0])
        return max_count
    for i in range(len(values) - 1):
        if abs(values[i] - values[i+1]) == 1 :
            curr = a.count(values[i]) + a.count(values[i + 1])
            if curr > max_count:
                max_count = curr
        else:
            curr = a.count(values[i])
            if curr > max_count:
                max_count = curr
        
    return max_count

print(pickingNumbers([6, 6, 6, 6, 6, 6]))