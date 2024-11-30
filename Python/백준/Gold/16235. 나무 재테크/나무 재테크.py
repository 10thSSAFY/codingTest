import sys
input = sys.stdin.readline

def solution():
    for r in range(N):
        for c in range(N):
            if not trees[r][c]:
                continue
            dead = 0
            grow = {}
            for age, cnt in sorted(trees[r][c].items()):
                alive = min(soil[r][c] // age, cnt)
                dead += age // 2 * (cnt - alive)
                if alive:
                    soil[r][c] -= alive * age
                    grow[age + 1] = alive
            soil[r][c] += dead
            trees[r][c] = grow

    for r in range(N):
        for c in range(N):
            tmp = 0
            for age in trees[r][c]:
                if age % 5 != 0:
                    continue
                tmp += trees[r][c][age]
            if tmp:
                for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < N and 0 <= nc < N):
                        continue
                    trees[nr][nc][1] = trees[nr][nc].get(1, 0) + tmp
            soil[r][c] += A[r][c]


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

soil = [[5] * N for _ in range(N)]
trees = [[dict() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1][z] = 1

for _ in range(K):
    solution()

result = 0
for r in range(N):
    for c in range(N):
        result += sum(trees[r][c].values())

print(result)