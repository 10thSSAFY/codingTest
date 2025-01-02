import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def cycle(r, c, color, start_r, start_c, depth):
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if not (0 <= nr < N and 0 <= nc < M):
            continue

        if (start_r, start_c) == (nr, nc) and depth >= 4:
            print('Yes')
            sys.exit()

        if arr[nr][nc] == color and not visit[nr][nc]:
            visit[nr][nc] = True
            cycle(nr, nc, color, start_r, start_c, depth + 1)
            visit[nr][nc] = False


def solution():
    global result
    for r in range(N - 1):
        for c in range(M - 1):
            visit[r][c] = True
            if cycle(r, c, arr[r][c], r, c, 1):
                result = 'Yes'
                return


N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
visit = [[False] * M for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
solution()

print('No')
