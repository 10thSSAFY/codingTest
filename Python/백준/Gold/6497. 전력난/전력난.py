import sys
input = sys.stdin.readline

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    graph = []
    parent = [i for i in range(m)]
    total_cost = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        graph.append((z, x, y))
        total_cost += z

    graph.sort()

    min_cost = 0
    for edge in graph:
        cost, a, b = edge
        if find(a) != find(b):
            union(a, b)
            min_cost += cost

    result = total_cost - min_cost
    print(result)