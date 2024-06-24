import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append((x, y))

result = []
for i in range(N):
    K = 1
    for j in range(N):
        if i == j:
            continue
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            K += 1
    result.append(K)

print(*result)
