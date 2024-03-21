CCTV = {
    1: [[(-1, 0)], [(1, 0)], [(0, -1)], [(0, 1)]],
    2: [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]],
    3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
    4: [[(0,-1), (-1,0), (0,1)], [(-1,0), (0,1), (1,0)], [(0,1), (1,0), (0,-1)], [(1,0), (0,-1), (-1,0)]],
    5: [[(-1, 0), (1, 0), (0, -1), (0, 1)]]
}


def dfs(iterate):
    global result

    if iterate == len_CCTVs:
        cnt = 0
        for line in arr:
            cnt += line.count(0)
        result = min(cnt, result)
        return

    num, r, c = CCTVs[iterate]
    for delta in CCTV[num]:
        tmp = []
        for dr, dc in delta:
            newR, newC = r, c
            while 0 <= newR + dr < N and 0 <= newC + dc < M and arr[newR + dr][newC + dc] != 6:
                newR, newC = newR + dr, newC + dc
                if arr[newR][newC] == 0:
                    tmp.append((newR, newC))
        for tr, tc in tmp:
            arr[tr][tc] = 8
        dfs(iterate + 1)
        for tr, tc in tmp:
            arr[tr][tc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

CCTVs = []
for r in range(N):
    for c in range(M):
        if arr[r][c] in [1, 2, 3, 4, 5]:
            CCTVs.append((arr[r][c], r, c))

len_CCTVs = len(CCTVs)

result = 2147843647
dfs(0)

print(result)