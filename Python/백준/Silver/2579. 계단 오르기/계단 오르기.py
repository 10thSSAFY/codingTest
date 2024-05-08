N = int(input())
lst = [0] * 301
for i in range(N):
    lst[i] = int(input())

dp = [0] * 301
dp[0] = lst[0]
dp[1] = lst[0] + lst[1]
dp[2] = max(lst[0] + lst[2], lst[1] + lst[2])

for i in range(3, N):
    dp[i] = max(lst[i] + dp[i-2], lst[i] + lst[i-1] + dp[i-3])

print(dp[N-1])