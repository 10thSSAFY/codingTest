import sys
input = sys.stdin.readline

dr = (-1, -1, -1, 0, 0, 1, 1, 1)
dc = (-1, 0, 1, -1, 1, -1, 0, 1)

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
seeds = [list(map(int, input().split())) for _ in range(M)]

soil = [[5] * N for _ in range(N)]
trees = [[dict() for _ in range(N)] for _ in range(N)]
for x, y, z in seeds:
    trees[x-1][y-1][z] = 1

for _ in range(K):
    for i in range(N):
        for j in range(N):
            if not trees[i][j]:
                continue
            soil_from_dead = 0
            grow_trees = {}
            for age, cnt in sorted(trees[i][j].items()):
                alive = min(soil[i][j] // age, cnt)
                soil_from_dead += age // 2 * (cnt - alive)
                if alive:
                    soil[i][j] -= alive * age
                    grow_trees[age+1] = alive
            soil[i][j] += soil_from_dead
            trees[i][j] = grow_trees

    for i in range(N):
        for j in range(N):
            tmp = 0
            for age in trees[i][j]:
                if age % 5 != 0:
                    continue
                tmp += trees[i][j][age]
            if tmp:
                for d in range(8):
                    nr = i + dr[d]
                    nc = j + dc[d]
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue
                    trees[nr][nc][1] = trees[nr][nc].get(1, 0) + tmp

            soil[i][j] += A[i][j]

ans = 0
for i in range(N):
    for j in range(N):
        ans += sum(trees[i][j].values())

print(ans)