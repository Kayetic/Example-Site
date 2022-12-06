# Non-Recursive function
def fibonacci(n):
    print("Fibonacci sequence:")
    a = 0
    b = 0
    while b <= n:
        c = a + b
        a = b
        b = c
        print(b)


fibonacci(10)


# Recursive function
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_recursive(n-1) + fibonacci_recursive(n-2))


def sum_even(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return n + sum_even(n-2)
    else:
        return sum_even(n-1)
