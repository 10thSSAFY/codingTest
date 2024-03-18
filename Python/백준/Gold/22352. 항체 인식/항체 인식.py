import sys
from collections import deque
input = sys.stdin.readline


def bfs(y, x, num):
    visited = [[False] * M for _ in range(N)]
    q = deque([(y, x)])
    visited[y][x] = True
    origin = before[y][x]

    while q:
        r, c = q.popleft()
        before[r][c] = num

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r+dr, c+dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            A, B, C = visited[nr][nc], before[nr][nc], before[y][x]
            if not visited[nr][nc] and before[nr][nc] == origin:
                q.append((nr, nc))
                visited[nr][nc] = True


def solution():
    for i in range(N):
        for j in range(M):
            if before[i][j] == after[i][j]:
                continue
            bfs(i, j, after[i][j])
            for r in range(N):
                for c in range(M):
                    if before[r][c] != after[r][c]:
                        print('NO')
                        return
            print('YES')
            return
    print('YES')
    return



N, M = map(int, input().split())
before = [list(map(int, input().strip().split())) for _ in range(N)]
after = [list(map(int, input().strip().split())) for _ in range(N)]

solution()