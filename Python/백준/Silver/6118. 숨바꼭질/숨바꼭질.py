input = __import__('sys').stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

visit = [-1] * (N + 1)
visit[1] = 0
q = deque([1])

result, dist, cnt = 1, 0, 1
while q:
    n = q.popleft()
    for v in graph[n]:
        if visit[v] == -1:
            visit[v] = visit[n] + 1
            if visit[n] + 1 > dist:
                result, dist, cnt = v, visit[n] + 1, 1
            elif visit[n] + 1 == dist:
                result, cnt = min(result, v), cnt + 1
            q.append(v)

print(result, dist, cnt)
