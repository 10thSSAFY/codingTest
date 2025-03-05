M = int(input())
N = int(input())

S = [False] * 10001
for i in range(1, 101):
    S[i**2] = True

res = []
for num in range(M, N + 1):
    if S[num]:
        res.append(num)

if res:
    print(sum(res))
    print(res[0])
else:
    print(-1)
            