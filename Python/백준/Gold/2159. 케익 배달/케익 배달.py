import sys
input = sys.stdin.readline

N = int(input())
sr, sc = map(int, input().split())
deliver = [(sr, sc)]
for _ in range(N):
    r, c = map(int, input().split())
    deliver.append((r, c))

dist = [[float('inf')] * 5 for _ in range(N + 1)]
dist[0] = [1, 1, 1, 1, 0]

dr = [-1, 0, 1, 0, 0]
dc = [0, 1, 0, -1, 0]
for i in range(1, N + 1):
    for d in range(5):
        r, c = deliver[i][0] + dr[d], deliver[i][1] + dc[d]
        for j in range(5):
            nr, nc = deliver[i - 1][0] + dr[j], deliver[i - 1][1] + dc[j]
            dist[i][d] = min(dist[i][d], abs(nr - r) + abs(nc - c) + dist[i - 1][j])

print(min(dist[-1]))
