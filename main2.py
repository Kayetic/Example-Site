# Description: Fibonacci sequence

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

# main function


def main():
    n = int(input("Enter a number: "))
    print("Fibonacci sequence:")
    for i in range(n):
        print(fibonacci(i))


# call main function
main()
