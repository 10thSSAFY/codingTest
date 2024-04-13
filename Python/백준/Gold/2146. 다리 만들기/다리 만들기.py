import sys
from collections import deque
input = sys.stdin.readline


def land(R, C, Num):
    arr[R][C] = Num
    q = deque([(R, C)])
    visited = [[False] * N for _ in range(N)]
    visited[R][C] = True
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] != 0:
                visited[nr][nc] = True
                arr[nr][nc] = Num
                q.append((nr, nc))


def bfs(n):
    global result
    check = [[-1] * N for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == n:
                q.append((i, j))
                check[i][j] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nr, nc = r+dr, c+dc
            if nr < 0 or nc < 0 or N <= nr or N <= nc:
                continue
            if arr[nr][nc] > 0 and arr[nr][nc] != n:
                result = min(result, check[r][c])
                return
            if arr[nr][nc] == 0 and check[nr][nc] == -1:
                check[nr][nc] = check[r][c] + 1
                q.append((nr, nc))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

Num = 1
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            Num += 1
            land(r, c, Num)

result = sys.maxsize
for i in range(2, Num+1):
    bfs(i)

print(result)