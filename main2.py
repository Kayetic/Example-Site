import whisper

model = whisper.load_model("base")

# Recursive function


def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_recursive(n-1) + fibonacci_recursive(n-2))

# Non-Recursive function


def fibonnaci_non_recursive(n):
    if n <= 1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b


def sum_even(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return n + sum_even(n-2)
    else:
        return sum_even(n-1)
