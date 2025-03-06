N, L = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

start = lst[0]
cnt = 1

for pos in lst[1:]:
    if pos in range(start, start + L):
        continue
    else:
        start = pos
        cnt += 1

print(cnt)
