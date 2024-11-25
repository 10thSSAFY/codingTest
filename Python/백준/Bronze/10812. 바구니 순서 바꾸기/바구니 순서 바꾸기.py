N, M = map(int, input().split())
lst = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j, k = map(int, input().split())
    tmp = lst[i - 1 : j]
    for r in range(k - i):
        tmp.append(tmp[0])
        tmp.remove(tmp[0])
    lst[i - 1 : j] = tmp

print(*lst)