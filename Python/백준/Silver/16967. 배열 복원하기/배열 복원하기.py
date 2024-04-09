H, W, X, Y = map(int, input().split())
arrB = [list(map(int, input().split())) for _ in range(H + X)]
for r in range(H):
    for c in range(W):
        arrB[r+X][c+Y] -= arrB[r][c]

for r in range(H):
    print(*arrB[r][:W])