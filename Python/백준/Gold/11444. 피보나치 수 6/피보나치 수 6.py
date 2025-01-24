import sys
sys.setrecursionlimit(10 ** 8)


def fibo(x):
    if x not in F:
        if x % 2 == 0:
            F[x] = (fibo(x // 2) * (fibo(x // 2) + 2 * fibo(x // 2 - 1))) % 1000000007
        else:
            F[x] = (fibo(x // 2) ** 2 + fibo(x // 2 + 1) ** 2) % 1000000007
    return F[x]


N = int(input())
F = dict()
F[0], F[1], F[2] = 0, 1, 1
fibo(N)

print(F[N])
