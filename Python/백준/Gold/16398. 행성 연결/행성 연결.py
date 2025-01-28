def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

parent = [i for i in range(N)]
edges = []

for r in range(N):
    for c in range(r + 1, N):
        edges.append((arr[r][c], r, c))
edges.sort()

result = 0
for edge in edges:
    w, s, e = edge

    if find(s) != find(e):
        union(s, e)
        result += w

print(result)