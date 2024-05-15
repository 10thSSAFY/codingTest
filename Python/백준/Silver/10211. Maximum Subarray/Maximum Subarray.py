T = int(input())
for _ in range(T):
    N = int(input())
    X = list(map(int, input().split()))

    result = [X[0]]

    for i in range(1, N):
        res = max(result[i-1] + X[i], X[i])
        result.append(res)

    print(max(result))