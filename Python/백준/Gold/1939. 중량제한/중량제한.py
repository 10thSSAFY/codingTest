from collections import deque
import sys
input = sys.stdin.readline


def bfs(m):
    visited[S] = True
    q = deque()
    q.append(S)
    
    while q:
        now = q.popleft()
        if now == E:
            return True
        for nN, nC in graph[now]:
            if visited[nN] == 0 and m <= nC:
                q.append(nN)
                visited[nN] = True

    return False


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
   
S, E = map(int, input().split())
l, r = 1, 1000000000
while l <= r:
    m = (l + r) // 2
    visited = [False] * (N + 1)
    if bfs(m):
        l = m + 1
    else:
        r = m - 1

print(r)
