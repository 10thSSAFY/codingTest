import sys
input = sys.stdin.readline

def roll(d):
    global Bottom, North, Top, South, West, East
    if d == 1:
        Bottom, North, Top, South, West, East = East, North, West, South, Bottom, Top
    elif d == 2:
        Bottom, North, Top, South, West, East = West, North, East, South, Top, Bottom
    elif d == 3:
        Bottom, North, Top, South, West, East = North, Top, South, Bottom, West, East
    elif d == 4:
        Bottom, North, Top, South, West, East = South, Bottom, North, Top, West, East


way = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}

N, M, r, c, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
Klst = list(map(int, input().split()))

Bottom, North, Top, South, West, East = 0, 0, 0, 0, 0, 0

Bottom = arr[r][c]
for do in Klst:
    dr, dc = way[do]
    newR, newC = r+dr, c+dc
    if 0 <= newR < N and 0 <= newC < M:
        r, c = newR, newC
        roll(do)
        if arr[r][c] != 0:
            Bottom = arr[r][c]
            arr[r][c] = 0
        else:
            arr[r][c] = Bottom
        print(Top)