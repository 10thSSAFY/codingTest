import heapq
import sys
input = sys.stdin.readline

dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]

cnt = 0
while True:
    n = int(input())

    if n == 0:
        break

    cnt += 1
    board = [list(map(int, input().split())) for _ in range(n)]
    heap = []
    dist = [[1e9] * n for _ in range(n)]
    dist[0][0] = board[0][0]
    heapq.heappush(heap, (board[0][0], 0, 0))

    while heap:
        distance, r, c = heapq.heappop(heap)

        if r == n - 1 and c == n - 1:
            print("Problem", str(cnt) + ":", distance)
            break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:
                cost = distance + board[nr][nc]
                if dist[nr][nc] > cost:
                    dist[nr][nc] = distance + board[nr][nc]
                    heapq.heappush(heap, (distance + board[nr][nc], nr, nc))