import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for r in range(1, N):
    for c in range(r + 1):
        if c == 0:
            arr[r][c] += arr[r-1][c]
        elif c == r:
            arr[r][c] += arr[r-1][c-1]
        else:
            arr[r][c] += max(arr[r-1][c-1], arr[r-1][c])

print(max(arr[N-1]))
