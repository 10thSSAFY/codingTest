H, W = map(int, input().split())
lst = list(map(int, input().split()))

result = 0
for h in range(H):
    flag = False
    cnt = 0
    for w in range(W):
        if lst[w] <= h:
            cnt += 1
        elif flag:
            result += cnt
            cnt = 0
        else:
            flag = True
            cnt = 0

print(result)
