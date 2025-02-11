N = int(input())
M = int(input())
arr = list(map(int, input().split()))

result = []

for i in arr:
    if i not in [x[0] for x in result]:
        if len(result) < N:
            result.append([i, 1])
        else:
            mn = min(result, key=lambda x: x[1])
            result.remove(mn)
            result.append([i, 1])
    else:
        for j in range(len(result)):
            if result[j][0] == i:
                result[j][1] += 1
                break

result.sort()
for i in result:
    print(i[0], end=' ')