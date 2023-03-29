

# write a fibbonaci function non recursive

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


fib(2000)


# write a fibbonaci function recursive

def fib2(n):
    if n < 2:
        return n
    return fib2(n-2) + fib2(n-1)


print(fib2(10))


# write a fibbonaci function recursive with memoization

def fib3(n, memo={}):
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fib3(n-2, memo) + fib3(n-1, memo)
    return memo[n]


print(fib3(10))
