from collections import deque


def bfs(s, g):
    if s == g:
        return 0

    q = deque([s])
    visited[s] = True
    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(q)):
            n = q.popleft()
            if 0 < n - D and not visited[n - D]:
                if n - D == g:
                    return cnt
                visited[n - D] = True
                q.append(n - D)
            if n + U <= F and not visited[n + U]:
                if n + U == g:
                    return cnt
                visited[n + U] = True
                q.append(n + U)

    return 'use the stairs'


F, S, G, U, D = map(int, input().split())

visited = [False] * (F + 1)
visited[0] = True

result = bfs(S, G)
print(result)