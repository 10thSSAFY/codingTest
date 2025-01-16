import heapq
import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 0
while True:
    N = int(input())
    if N == 0:
        break

    cnt += 1
    arr = [list(map(int, input().split())) for _ in range(N)]
    dist = [[float('inf')] * N for _ in range(N)]

    dist[0][0] = arr[0][0]
    hq = []
    heapq.heappush(hq, (arr[0][0], 0, 0))

    while hq:
        d, r, c = heapq.heappop(hq)
        if (r, c) == (N - 1, N - 1):
            print(f'Problem {cnt}: {dist[r][c]}')
            break

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            if dist[nr][nc] > dist[r][c] + arr[nr][nc]:
                dist[nr][nc] = dist[r][c] + arr[nr][nc]
                heapq.heappush(hq, (dist[nr][nc], nr, nc))
