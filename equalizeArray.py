

def equalizeArray(arr):
    aux = [arr.count(i) for i in arr]
    return len(arr) - max(aux)

arr = [3, 3, 2, 1, 3]
print(equalizeArray(arr))