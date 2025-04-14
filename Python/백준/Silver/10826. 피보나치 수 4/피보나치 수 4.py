N = int(input())

if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    a, b, res = 0, 1, 1
    for _ in range(N - 1):
        res = a + b
        a, b = b, res
    print(res)