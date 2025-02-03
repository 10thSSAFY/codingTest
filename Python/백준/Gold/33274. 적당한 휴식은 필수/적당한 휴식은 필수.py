N = int(input())
arr = [[0] * N for _ in range(N)]

for i in range(N // 2):
    arr[i * 2][i * 2] = i * 2
    arr[i * 2][i * 2 + 1] = i * 2
    arr[i * 2 + 1][i * 2] = i * 2 + 1
    arr[i * 2 + 1][i * 2 + 1] = i * 2 + 2

if N % 2 == 1:
    arr[N - 1][N - 1] = N * 2 - 2


for a in arr:
    print(*a)
