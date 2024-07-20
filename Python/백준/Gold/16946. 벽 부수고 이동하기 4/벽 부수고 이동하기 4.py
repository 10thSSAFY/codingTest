from collections import deque
input = __import__('sys').stdin.readline


def bfs(start):
    q = deque([start])
    cnt = 1
    while q:
        r, c = q.popleft()
        zeros[r][c] = group
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if visited[nr][nc] or arr[nr][nc] == 1:
                continue
            visited[nr][nc] = True
            q.append((nr, nc))
            cnt += 1
    return cnt


N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
zeros = [[0] * M for _ in range(N)]

group = 1
info = dict()
info[0] = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            w = bfs((i, j))
            info[group] = w
            group += 1


for r in range(N):
    for c in range(M):
        addList = set()
        if arr[r][c]:
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < N and 0 <= nc < M):
                    continue
                addList.add(zeros[nr][nc])

            for add in addList:
                arr[r][c] += info[add]
                arr[r][c] %= 10

for a in arr:
    print("".join(map(str, a)))
