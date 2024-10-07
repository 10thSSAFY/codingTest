N = int(input())
lst = []
dp = [1] * N

for _ in range(N):
    A, B = map(int, input().split())
    lst.append((A, B))

lst.sort()

for i in range(1, N):
    for j in range(0, i):
        if lst[j][1] < lst[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
