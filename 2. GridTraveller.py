# Number of ways to travel from top left to bottom right in a grid of size mxn and we can only move bottom and right

def GridTraveller(m,n, memo = {}):
    if(f'{m}_{n}' in list(memo.keys())):
        return memo[f'{m}_{n}']
    if(m == 0 or n == 0):
        return 0
    if(m == 1 or n == 1):
        return 1
    else:
        memo[f'{m}_{n}'] = GridTraveller(m-1,n, memo) + GridTraveller(m,n-1, memo)
        memo[f'{n}_{m}'] = memo[f'{m}_{n}']
        return memo[f'{m}_{n}']

m = int(input('Enter the number of rows in Grid?\n'))
n = int(input('Enter the number of columns in Grid?\n'))
print(f'No. of ways to travel in {m}x{n} grid is {GridTraveller(m,n)}')