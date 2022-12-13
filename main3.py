import time

# Recursive fibonacci function


def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_recursive(n-1) + fibonacci_recursive(n-2))


# measure the time it takes to run the function
startTime = time.process_time()
# use the function for the number 10
fibonacci_recursive(40)
endTime = time.process_time()

print("Time taken to run the function: ", endTime - startTime)
