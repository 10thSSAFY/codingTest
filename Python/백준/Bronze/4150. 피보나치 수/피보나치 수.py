N = int(input())

if N == 1: print(1)
elif N == 2: print(1)
else:
    a, b, r = 1, 1, 2
    for _ in range(N - 3):
        a, b, r = b, r, b + r
    print(r)