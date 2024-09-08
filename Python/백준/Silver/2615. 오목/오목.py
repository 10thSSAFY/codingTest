def check(R, C):
    global win, flag, ans
    color = arr[R][C]

    for d in D:
        cnt = 1
        for i in range(5):
            nr, nc = R + d[i][0], C + d[i][1]
            if not (0 <= nr < 19 and 0 <= nc < 19):
                break
            if arr[nr][nc] != color:
                break
            cnt += 1

        if cnt == 5 and color != arr[R + d[5][0]][C + d[5][1]]:
            flag = True
            win = color
            ans = (R, C)
            return


D = [((-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), ( 1, -1)),
     (( 1, 0), ( 2, 0), ( 3, 0), ( 4, 0), ( 5, 0), (-1,  0)),
     (( 1, 1), ( 2, 2), ( 3, 3), ( 4, 4), ( 5, 5), (-1, -1)),
     (( 0, 1), ( 0, 2), ( 0, 3), ( 0, 4), ( 0, 5), ( 0, -1))]

arr = [list(map(int, input().split())) for _ in range(19)]

win = False
ans = (-1, -1)
flag = False

for r in range(19):
    for c in range(19):
        if arr[r][c] != 0:
            check(r, c)
        if flag:
            break
    if flag:
        break

if win:
    print(win)
    print(ans[0] + 1, ans[1] + 1)
else:
    print(0)