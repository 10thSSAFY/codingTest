def solution2():
    point = 0
    nr, nc = r1, c1
    for dr, dc in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
        while (0 <= nr + dr < R and 0 <= nc + dc < C):
            if arr[nr + dr][nc + dc] == -1:
                break
            arr[nr + dr][nc + dc], point = point, arr[nr + dr][nc + dc]
            nr += dr
            nc += dc

    point = 0
    nr, nc = r2, c2
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        while (0 <= nr + dr < R and 0 <= nc + dc < C):
            if arr[nr + dr][nc + dc] == -1:
                break
            arr[nr + dr][nc + dc], point = point, arr[nr + dr][nc + dc]
            nr += dr
            nc += dc


def solution1():
    tmp = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if arr[r][c] > 0:
                cnt = 0
                for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < R and 0 <= nc < C):
                        continue
                    if arr[nr][nc] == -1:
                        continue
                    cnt += 1
                    tmp[nr][nc] += arr[r][c] // 5
                arr[r][c] -= (arr[r][c] // 5) * cnt

    for r in range(R):
        for c in range(C):
            if tmp[r][c]:
                arr[r][c] += tmp[r][c]


def check():
    for r in range(R):
        for c in range(C):
            if arr[r][c] == -1:
                return (r, c, r + 1, c)


R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

(r1, c1, r2, c2) = check()

for _ in range(T):
    solution1()
    solution2()

result = 0
for i in range(R):
    result += sum(arr[i])

print(result + 2)