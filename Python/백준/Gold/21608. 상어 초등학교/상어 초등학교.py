N = int(input())
arr = [[0] * N for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
data = dict()
for _ in range(N * N):
    num, *lst = map(int, input().split())
    S = set(lst)
    data[num] = S
    info = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                like, empty = 0, 0
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if not(0 <= nr < N and 0 <= nc < N):
                        continue
                    if arr[nr][nc] in S:
                        like += 1
                    if arr[nr][nc] == 0:
                        empty += 1
                info.append((r, c, like, empty))

    info.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    arr[info[0][0]][info[0][1]] = num

result = 0
score = [0, 1, 10, 100, 1000]

for r in range(N):
    for c in range(N):
        tmp = 0
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not(0 <= nr < N and 0 <= nc < N):
                continue
            if arr[nr][nc] in data[arr[r][c]]:
                tmp += 1
        result += score[tmp]
print(result)