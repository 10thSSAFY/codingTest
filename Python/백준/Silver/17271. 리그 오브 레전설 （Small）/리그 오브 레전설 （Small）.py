N, B = map(int, input().split())

MOD = 1000000007
dp = [1] * (N + 1)
for i in range(B, N + 1):
    dp[i] = (dp[i - 1] + dp[i - B]) % MOD

print(dp[N])
