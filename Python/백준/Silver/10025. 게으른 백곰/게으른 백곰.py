import sys
input = sys.stdin.readline


N, K = map(int, input().split())
lst = [0] * 1000001
for _ in range(N):
    g, k = map(int, input().split())
    lst[k] = g

interval = K * 2 + 1
result = sum_num = sum(lst[:interval])

for j in range(interval, 1000001):
    sum_num += lst[j] - lst[j-interval]
    result = max(result, sum_num)

print(result)