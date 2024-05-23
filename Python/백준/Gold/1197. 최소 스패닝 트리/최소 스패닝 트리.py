import sys
input = sys.stdin.readline


def union(a, b):
    a, b = parent[a], parent[b]
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


V, E = map(int, input().split())
parent = [i for i in range(V+1)]
lst = []
for _ in range(E):
    A, B, C = map(int, input().split())
    lst.append((C, A, B))

lst.sort()

result = 0
for (cost, nodeA, nodeB) in lst:
    if find(nodeA) != find(nodeB):
        union(nodeA, nodeB)
        result += cost

print(result)