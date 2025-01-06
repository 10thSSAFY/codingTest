N = int(input())
M = int(input())

lst = [True] * N
for _ in range(M):
    lst[int(input()) - 1] = False

dp = [1] * 41
dp[2] = 2
dp[3] = 3
for i in range(4, 41):
    dp[i] = dp[i - 1] + dp[i - 2]

result = 1
tmp = 0
for i in range(N):
    if lst[i]:
        tmp += 1
    else:
        result *= dp[tmp]
        tmp = 0
result *= dp[tmp]

print(result)