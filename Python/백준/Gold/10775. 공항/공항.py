import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def union(x, y):
    x = find(x)
    y = find(y)
    parent[x] = y


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


G = int(input())
P = int(input())

parent = [i for i in range(G + 1)]

result = 0
for _ in range(P):
    x = find(int(input()))
    if x == 0:
        break

    union(x, x - 1)
    result += 1

print(result)