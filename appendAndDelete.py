def appendAndDelete(s, t, k):
    # Write your code here
    given = list(s)
    gLen = len(given)
    target = list(t)
    tLen = len(t)
    
    ops = 0
    
    if gLen < tLen:
        while tLen != 0:
            try:
                if target[tLen -1] == given[tLen - 1]:
                    #operations remain the same
                    ops = ops
                    #Decrease tLen
                    tLen -=1
                else:
                    #Add append and delete operation to ops if the characters are not the same
                    ops += 2
                    #Decrease tLen
                    tLen -=1
            except:
                #When out of bounds exception occurs, add one opperation (An append operation to given list)
                tLen -= 1
                ops += 1
    elif gLen > tLen:
        while gLen != 0:
            try:
                if given[gLen -1] == target[gLen - 1]:
                    #operations remain the same
                    ops = ops
                    #Decrease gLen
                    gLen -= 1
                else:
                    #Add append and delete operation to ops if the characters are not the same
                    ops += 2
                    gLen -= 1
            except:
                #When out of bounds exception occurs, add one opperation (An delete operation to given list)
                ops += 1
                given.pop()
                #Resert value of gLen
                gLen = len(given)
    elif gLen == tLen:
        start = 0
        while start != gLen:
            if target[start] == given[start]:
                ops = ops
                start += 1
            else:
                '''
                When the characters are not equal, we will have to change all subsequent characters in the given list
                To get number of operations we get the length of characters to be changed * 2 (append and delete operations)
                '''
                ops = len(given[start:]) * 2
                start = gLen
        if ops > k:
            return 'No'
        else:
            return 'Yes'
    
    if k%2 != 0 and ops%2 != 0 or k%2 != 0 and ops%2 == 0 or ops%2 == 0:
        return('Yes')
    elif k%2 == 0 and ops%2 != 0 or k%2 == 0 and ops%2 == 0:
        return('No')