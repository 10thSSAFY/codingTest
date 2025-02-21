N, Q = map(int, input().split())
A = list(map(int, input().split()))
dp = []
result = 0
for i in range(N):
    tmp = A[i] * A[(i + 1) % N] * A[(i + 2) % N] * A[(i + 3) % N]
    dp.append(tmp)
    result += tmp

q = list(map(int, input().split()))
for qi in q:
    qi -= 1
    if qi == -1:
        qi = N - 1
    for j in range(4):
        dp[qi] = -dp[qi]
        result += 2 * dp[qi]
        qi -= 1
        if qi == -1:
            qi = N - 1
    print(result)
