n = int(input())
s, e = 0, 3037000500
res = 0
while s <= e:
    m = (s + e) // 2
    if n > m ** 2:
        s = m + 1
    elif n <= m ** 2:
        res = m
        e = m - 1

print(res)