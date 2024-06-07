import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

dp = [-1001] * N
dp[0] = lst[0]

for i in range(1, N):
    dp[i] = max(dp[i-1] + lst[i], lst[i])

print(max(dp))