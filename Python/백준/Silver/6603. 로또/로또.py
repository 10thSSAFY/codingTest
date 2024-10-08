def dfs(depth, idx):
    if depth == 6:
        print(*out)
        return

    for i in range(idx, k):
        out.append(S[i])
        dfs(depth + 1, i + 1)
        out.pop()


while True:
    array = list(map(int, input().split()))
    k = array[0]
    S = array[1:]
    out = []
    dfs(0, 0)
    if k == 0:
        exit()
    print()