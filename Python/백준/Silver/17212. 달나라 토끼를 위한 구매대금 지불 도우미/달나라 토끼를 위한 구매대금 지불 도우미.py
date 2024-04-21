N = int(input())

dp = [2147483647] * (N + 1)
dp[0] = 0
for i in range(1, N+1):
    dp[i] = dp[i-1] + 1
    if i >= 2:
        dp[i] = min(dp[i], dp[i-2] + 1)
    if i >= 5:
        dp[i] = min(dp[i], dp[i-5] + 1)
    if i >= 7:
        dp[i] = min(dp[i], dp[i-7] + 1)

print(dp[N])