def solution():
    global win, R, C

    for r in range(19):
        for c in range(19):
            if arr[r][c] != 0:
                color = arr[r][c]
                for dr, dc in D:
                    cnt = 1
                    nr, nc = r + dr, c + dc

                    while True:
                        if not (0 <= nr < 19 and 0 <= nc < 19) or arr[nr][nc] != color:
                            break
                        cnt += 1
                        nr, nc = nr + dr, nc + dc

                    if cnt == 5:
                        if not (0 <= r - dr < 19 and 0 <= c - dc < 19 and arr[r - dr][c - dc] == color):
                            win = color
                            R, C = r + 1, c + 1
                            return


arr = [list(map(int, input().split())) for _ in range(19)]

D = [(-1, 1), (0, 1), (1, 1), (1, 0)]

win = False
R, C = 0, 0

solution()

if win:
    print(win)
    print(R, C)
else:
    print(0)