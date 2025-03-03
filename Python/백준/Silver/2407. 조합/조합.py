def nCr(n, r):
    if n == 1:
        return 1
    elif n == r or r == 0:
        return 1
    else:
        if arr[n][r] == -1:
            arr[n][r] = nCr(n - 1, r) + nCr(n - 1, r - 1)
        return arr[n][r]


N, M = list(map(int, input().split()))
arr = [[-1 for j in range(M + 1)] for i in range(N + 1)]
result = nCr(N, M)

print(result)
