def fibonacci(n):
    return n-2


def fib(n):
    a, b = 1, 1
    for i in range(3, n+1):
        a, b = b, a+b

    return b


n = int(input())
res1 = fib(n)
res2 = fibonacci(n)
print(res1, res2)