def fib(n):
    if n < 3:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))