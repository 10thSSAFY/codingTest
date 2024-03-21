import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    parent[find(y)] = find(x)


N = int(input())
M = int(input())

parent = [i for i in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    union(i, j)

cnt = 0
for k in range(2, N+1):
    if find(k) == find(1):
        cnt += 1

print(cnt)