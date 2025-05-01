N = int(input())
lst = list(map(int, input().split()))

left = 0
D = dict()
result = 0

for i in range(N):
    f = lst[i]

    if f in D:
        D[f] += 1
    else:
        D[f] = 1

    while len(D) > 2:
        r = lst[left]
        D[r] -=1

        if D[r] == 0:
            del D[r]

        left += 1

    result = max(result, i - left + 1)

print(result)