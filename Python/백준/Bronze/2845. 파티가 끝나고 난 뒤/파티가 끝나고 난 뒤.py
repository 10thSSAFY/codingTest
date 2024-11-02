L, P = map(int, input().split())
lst = list(map(int, input().split()))

v = L * P
for i in range(5):
    lst[i] = lst[i] - v

print(*lst)