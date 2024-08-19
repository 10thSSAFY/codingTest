def find(s, e, v):
    while s < e:
        m = (s + e) // 2
        if LIS[m] < v:
            s = m + 1
        else:
            e = m
    return e


N = int(input())
lst = list(map(int, input().split()))
LIS = [lst[0]]

for i in range(1, N):
    if lst[i] > LIS[-1]:
        LIS.append(lst[i])
    else:
        idx = find(0, len(LIS), lst[i])
        LIS[idx] = lst[i]

print(len(LIS))
