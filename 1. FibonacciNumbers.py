# Fibonacci Series 1,1,2,3,5,...


def Fibonacci(n, memo = {}):
    if(n in list(memo.keys())):
        return memo[n]
    if(n<=2):
        return 1
    else:
        memo[n] = Fibonacci(n-1, memo) + Fibonacci(n-2, memo)
        return memo[n]

n = int(input('Enter the fibonacci number you want ?\n'))
print(f'{n}th Fibonacci number is {Fibonacci(n)}')