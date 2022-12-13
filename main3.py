# factorial of a number
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


def main():
    print(fact(27))


if __name__ == "__main__":
    main()

print("Why do we write __name__ == '__main__' ?")
print("Because we want to run the main() function only when we run the file directly,")
print("and not when we import it from another file.")
