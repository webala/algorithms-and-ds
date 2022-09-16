def getGCD(n1, n2):
    print('n1: ', n1, ' n2: ', n2)
    if n2 == 0:
        return n1
    return getGCD(n2, n1 % n2)

def getLCM(n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    else:
        gcd = getGCD(n1, n2)
        return abs(n1 * n2) / gcd


def getTotalX(a, b):
    result = 0

    lcm = a[0]
    for i in a:
        lcm = getLCM(lcm, i)
    
    gcd = b[0]
    for i in b:
        gcd = getGCD(gcd, i)
    
    multiple = 0
    while multiple <= gcd:
        multiple += lcm

        if gcd % multiple == 0:
            result += 1
        
    return result

a = [2, 4]
b = [16, 32, 96]

print(getTotalX(a, b))

