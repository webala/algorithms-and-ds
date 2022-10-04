import math
def jumpingOnClouds(c):
    # Write your code here
    jumps = 0
    i = 0
    while i < n-1:
        if i + 2 < n and c[i+2] == 0:
            jumps += 1
            i += 2
        elif i + 1 < n and c[i + 1] == 0:
            jumps += 1
            i += 1
            
    return jumps

c = [0, 0 ,1, 0, 0, 0, 0, 1, 0, 0]
print(jumpingOnClouds(c))