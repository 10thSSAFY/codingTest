res1 = 0
res2 = 100

for _ in range(7):
    N = int(input())
    if N % 2 == 1:
        res1 += N
        res2 = min(res2, N)

if res1 != 0:
    print(res1)
    print(res2)
else:
    print(-1)
