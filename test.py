#!python3


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():
    n = fib(10)
    print("fib(10) = %s" % (n))

main()

