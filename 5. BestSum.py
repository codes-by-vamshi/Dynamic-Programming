#  From given numbers, can you sum and make a target number with repetition? Return the numbers you added with smallest size

def BestSum(m,arr, memo = {}):
    if(m in list(memo.keys())):
        return memo[m]
    if(m == 0):
        return []
    if(m < 0):
        return None
    final = None
    for i in arr:
        outp = BestSum(m-i,arr, memo)
        if(outp != None):
            combination = outp + [i]
            if((final == None) or (len(final) > len(combination))):
                final = combination
    memo[m] = final
    return final

print(BestSum(100,[1,2,5,25]))