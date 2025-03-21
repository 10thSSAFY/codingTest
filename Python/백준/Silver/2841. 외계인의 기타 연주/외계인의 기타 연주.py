input = __import__('sys').stdin.readline


N, P = map(int, input().split())
lst = [[0] for _ in range(7)]
cnt = 0
for _ in range(N):
    n, p = map(int, input().split())
    if lst[n][-1] < p:
        lst[n].append(p)
        cnt += 1
    else:
        while lst[n][-1] > p:
            lst[n].pop()
            cnt += 1
        if lst[n][-1] == p:
            continue
        lst[n].append(p)
        cnt += 1
print(cnt)