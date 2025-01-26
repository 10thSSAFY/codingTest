import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def union(A, B):
    A = find(A)
    B = find(B)
    if A < B:
        parent[B] = A
    else:
        parent[A] = B


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


V, E = map(int, input().split())
parent = [i for i in range(V + 1)]
tree = []
result = 0

for _ in range(E):
    A, B, W = map(int, input().split())
    tree.append((W, A, B))
tree.sort()

for edge in tree:
    (W, A, B) = edge
    if find(A) != find(B):
        union(A, B)
        result += W

print(result)
