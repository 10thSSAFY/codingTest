N, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

s, e = 0, N - 1
result = 0

while s < e:
    if data[s] + data[e] <= K:
        s += 1; e -= 1
        result += 1
    else:
        e -= 1

print(result)