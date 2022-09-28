

def nonDivisibleSet(k, s):
    m = {}

    for i in s:
        if (i % k) in m.keys():
            m[i % k] += 1
        else:
            m[i % k] = 1
    
    ans = 0
    #Can only take one value with modulus 0 because two values with moduls 0 will be divisible by k
    if 0 in m.keys() and  m[0] > 0:
        ans += 1
    
    for i in range(1, k+1):
        if i in m.keys():
            if m[i] == 0:#leave values with modulus 0
                continue
            if i + i == k: # If a value can complement itself and be divisible by k we only take one
                ans += 1
            else:
                #Check two numbers that complement themselves and pick the one with maximum values
                if (k-i) in m.keys():
                    ans += max(m[i], m[k-i])
                    # initialize the count to zero so as not to add them again
                    m[i] = 0
                    m[k-i] = 0
                else:
                    ans += m[i]
                    m[i] = 0
    
    return ans


k = 3
s = [1, 7, 2, 4]

print(nonDivisibleSet(k, s))