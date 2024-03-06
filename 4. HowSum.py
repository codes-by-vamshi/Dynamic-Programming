# From given numbers, can you sum and make a target number with repetition? Return the numbers you added

def HowSum(m, arr, memo = {}):
    if(m in list(memo.keys())):
        return memo[m]
    if(m == 0):
        return []
    if(m < 0):
        return None
    for i in arr:
        outp = HowSum(m-i,arr)
        if(outp != None):
            outp.append(i)
            memo[m] = outp
            return outp
    memo[m] = None
    return None

print(HowSum(300,[7,14]))