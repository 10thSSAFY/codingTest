N = int(input())
dp = [float('inf')] * (N + 1)
dp[0] = 0

for i in range(N):
    if dp[i] != float('inf'):
        if i + 2 <= N:
            dp[i + 2] = min(dp[i + 2], dp[i] + 1)
        if i + 5 <= N:
            dp[i + 5] = min(dp[i + 5], dp[i] + 1)

if dp[N] != float('inf'):
    print(dp[N])
else:
    print(-1)
