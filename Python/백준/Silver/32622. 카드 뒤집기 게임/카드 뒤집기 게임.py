N = int(input())
lst = list(map(int, input().split()))

dp = []
cnt = 0
tmp = lst[0]
for num in lst:
    if (tmp != num):
        dp.append(cnt)
        tmp = num
        cnt = 1
    else:
        cnt += 1
dp.append(cnt)

result = max(dp)
for i in range(len(dp) - 1):
    result = max(result, dp[i] + dp[i + 1])

print(result)