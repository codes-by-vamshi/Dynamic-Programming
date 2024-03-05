# Check if we can form the number using sum of any number of times the given array numbers. Repetition is allowed. Numbers in array are all positive

def CanSum(m, arr, memo = {}):
    if(m in list(memo.keys())):
        return memo[m]
    if(m == 0):
        return True
    if(m < 0):
        return False
    for i in arr:
        if(CanSum(m-i, arr, memo)):
            memo[m-i] = True
            return True
    memo[m] = False
    return False

m = int(input('Enter your target number:\n'))
n = int(input('Enter the number of numbers in array:\n'))
arr = []
while n>0:
    n-=1
    arr.append(int(input('Enter the numbers for array\n')))
print(f'{m} can be formed by {arr} - {CanSum(m,arr)}')