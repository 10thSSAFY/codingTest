N = int(input())
dp = [1] * 10
tmp = [0] * 10

for _ in range(1, N):
    for i in range(10):
        tmp[i] = sum(dp[i : 10])
    for i in range(10):
        dp[i] += tmp[i]
    dp = tmp[:]

print(sum(dp) % 10007)
