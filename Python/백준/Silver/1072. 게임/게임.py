X, Y = map(int, input().split())
Z = (Y * 100) // X

s, e = 1, X
result = -1
while s <= e:
    m = (s + e) // 2
    if (Y + m) * 100 // (X + m) > Z:
        result = m
        e = m - 1
    else:
        s = m + 1

print(result)