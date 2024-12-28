N = int(input())
lst = list(map(int, input().split()))
tmp = 0
result = []
for i in range(N - 1):
    if lst[i] < lst[i+1]:
        tmp += lst[i+1] - lst[i]
    else:
        result.append(tmp)
        tmp = 0
result.append(tmp)
print(max(result))