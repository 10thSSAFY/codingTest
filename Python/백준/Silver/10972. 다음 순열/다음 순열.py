import sys

N = int(input())
lst = list(map(int, input().split()))
for i in range(N - 1, 0, -1):
    if lst[i - 1] < lst[i]:
        target = i - 1
        break
else:
    print(-1)
    sys.exit()

for i in range(N - 1, 0, -1):
    if lst[target] < lst[i]:
        lst[target], lst[i] = lst[i], lst[target]
        lst = lst[:target + 1] + sorted(lst[target + 1:])
        print(*lst)
        break