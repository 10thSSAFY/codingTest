N, Q = map(int, input().split())
A = list(map(int, input().split()))
dp = []
result = 0
for i in range(N):
    tmp = 1
    if i >= N:
        a1 = i % (N - 1) - 1
    else:
        a1 = i

    if i + 1 >= N:
        a2 = (i + 1) % (N - 1) - 1
    else:
        a2 = i + 1

    if i + 2 >= N:
        a3 = (i + 2) % (N - 1) - 1
    else:
        a3 = i + 2

    if i + 3 >= N:
        a4 = (i + 3) % (N - 1) - 1
    else:
        a4 = i + 3

    tmp *= A[a1]
    tmp *= A[a2]
    tmp *= A[a3]
    tmp *= A[a4]
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
