def solution(depth):
    if depth == max_depth:
        for line in arr:
            print(*line)
        exit()

    nr, nc = zeros[depth]
    nsq = (nc // 3) * 3 + nr // 3
    for i in range(1, 10):
        if not row[nc][i] and not col[nr][i] and not square[nsq][i]:
            row[nc][i] = True
            col[nr][i] = True
            square[nsq][i] = True
            arr[nc][nr] = i
            solution(depth + 1)
            row[nc][i] = False
            col[nr][i] = False
            square[nsq][i] = False


arr = [[False] * 9 for _ in range(9)]
row = [[False] * 10 for _ in range(9)]
col = [[False] * 10 for _ in range(9)]
square = [[False] * 10 for _ in range(9)]

zeros = []
for i in range(9):
    lst = list(map(int, input().split()))
    for j in range(9):
        arr[i][j] = lst[j]
        if lst[j]:
            row[i][lst[j]] = True
            col[j][lst[j]] = True
            square[(i // 3) * 3 + (j // 3)][lst[j]] = True
        else:
            zeros.append((j, i))

max_depth = len(zeros)

solution(0)