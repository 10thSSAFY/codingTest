N, M = map(int, input().split())
arr = list(input() for _ in range(N))
dp = [[0] * M for _ in range(N)]
res = 0

for i in range(N):
    for j in range(M):
        if i == 0 or j == 0:
            dp[i][j] = int(arr[i][j])
        elif arr[i][j] == '0':
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        res = max(res, dp[i][j])

print(res ** 2)
