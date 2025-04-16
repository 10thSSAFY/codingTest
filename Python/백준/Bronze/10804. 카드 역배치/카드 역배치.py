lst = [i for i in range(21)]
for _ in range(10):
    l, r = map(int, input().split())
    lst[l:r+1] = lst[r:l-1:-1]

print(*lst[1:])