import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H + X)]
for r in range(H):
    arr[r+X][Y:W+Y] = [b - a for a, b in zip(arr[r][:W], arr[r+X][Y:W+Y])]

for r in range(H):
    print(*arr[r][:W])