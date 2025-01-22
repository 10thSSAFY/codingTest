import sys
input = sys.stdin.readline

N = int(input())

lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append((x, y))

total = 0
for i in range(N - 1):
    total += abs(lst[i][0] - lst[i + 1][0]) + abs(lst[i][1] - lst[i + 1][1])

max_len = 0
for i in range(1, N - 1):
    d1 = abs(lst[i - 1][0] - lst[i][0]) + abs(lst[i - 1][1] - lst[i][1])
    d2 = abs(lst[i][0] - lst[i + 1][0]) + abs(lst[i][1] - lst[i + 1][1])
    d3 = abs(lst[i - 1][0] - lst[i + 1][0]) + abs(lst[i - 1][1] - lst[i + 1][1])
    max_len = max(max_len, d1 + d2 - d3)

result = total - max_len
print(result)
