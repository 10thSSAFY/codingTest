def calc6():
    global board
    N, M = len(board), len(board[0])
    tmp = [[0] * M for _ in range(N)]
    for r in range(N // 2, N):
        for c in range(M // 2):
            tmp[r][c + M //2] = board[r][c]
    for r in range(N // 2):
        for c in range(M // 2):
            tmp[r + N // 2][c] = board[r][c]
    for r in range(N // 2):
        for c in range(M // 2, M):
            tmp[r][c - M // 2] = board[r][c]
    for r in range(N // 2, N):
        for c in range(M // 2, M):
            tmp[r - N // 2][c] = board[r][c]
    return tmp


def calc5():
    global board
    N, M = len(board), len(board[0])
    tmp = [[0] * M for _ in range(N)]
    for r in range(N // 2, N):
        for c in range(M // 2):
            tmp[r - N // 2][c] = board[r][c]
    for r in range(N // 2):
        for c in range(M // 2):
            tmp[r][c + M // 2] = board[r][c]
    for r in range(N // 2):
        for c in range(M // 2, M):
            tmp[r + N // 2][c] = board[r][c]
    for r in range(N // 2, N):
        for c in range(M // 2, M):
            tmp[r][c - M // 2] = board[r][c]
    return tmp


def calc4():
    global board
    N, M = len(board), len(board[0])
    tmp = []
    for c in range(M - 1, -1, -1):
        line = []
        for r in range(N):
            line.append(board[r][c])
        tmp.append(line)
    return tmp


def calc3():
    global board
    N, M = len(board), len(board[0])
    tmp = []
    for c in range(M):
        line = []
        for r in range(N - 1, -1, -1):
            line.append(board[r][c])
        tmp.append(line)

    return tmp


def calc2():
    N, M = len(board), len(board[0])
    for r in range(N):
        board[r] = board[r][::-1]


def calc1():
    N, M = len(board), len(board[0])
    for r in range(N // 2):
        board[r], board[N - 1 - r] = board[N - 1 - r], board[r]


N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cmd = list(map(int, input().split()))
for c in cmd:
    if c == 1:
        calc1()
    elif c == 2:
        calc2()
    elif c == 3:
        board = calc3()
    elif c == 4:
        board = calc4()
    elif c == 5:
        board = calc5()
    elif c == 6:
        board = calc6()

for line in board:
    print(*line)