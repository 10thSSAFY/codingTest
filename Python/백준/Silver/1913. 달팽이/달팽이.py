N = int(input())
M = int(input())

arr = [[0] * N for _ in range(N)]
r, c = N // 2, N // 2

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

d = 3
result = [-1, -1]
for i in range(1, N * N + 1):
    arr[r][c] = i
    if i == M:
        result = [r + 1, c + 1]
    nr = r + dr[(d + 1) % 4]
    nc = c + dc[(d + 1) % 4]
    if arr[nr][nc] == 0:
        r, c = nr, nc
        d = (d + 1) % 4
    else:
        r += dr[d]
        c += dc[d]

for line in arr:
    print(*line)
print(*result)
