N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
_, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

arr = [[] for _ in range(N)]
for i in range(N):
    for j in range(K):
        num = 0
        for k in range(M):
            num += A[i][k] * B[k][j]
        arr[i].append(num)

for line in arr:
    print(*line)
