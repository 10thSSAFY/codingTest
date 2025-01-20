N, C = map(int, input().split())
lst = list(map(int, input().split()))

D = dict()
for i in range(N):
    if lst[i] in D:
        D[lst[i]][0] += 1
    else:
        D[lst[i]] = [1, i]

result = []
sorted_D = sorted(D.items(), key=lambda item: (-item[1][0], item[1][1]))
for tpl in sorted_D:
    N, cnt = tpl[0], tpl[1][0]
    for _ in range(cnt):
        result.append(N)

print(*result)
