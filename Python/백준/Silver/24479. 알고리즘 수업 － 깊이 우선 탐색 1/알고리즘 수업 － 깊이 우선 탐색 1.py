import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(graph, v, visited):
    global c
    visited[v] = c

    for i in graph[v]:
        if visited[i] == 0:
            c += 1
            dfs(graph, i, visited)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

c = 1

for i in range(m):
    a, b = (map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()

dfs(graph, r, visited)

for i in range(1, n + 1):
    print(visited[i])
