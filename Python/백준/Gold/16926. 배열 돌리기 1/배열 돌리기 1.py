from collections import deque

N, M, R = map(int, input().split())
A = [input().split() for _ in range(N)]

result = [[0] * M for _ in range(N)]
queue = deque()

depth = min(N, M) // 2
for d in range(depth):
    queue.clear()
    queue.extend(A[d][d : M - d])
    queue.extend([row[M - d - 1] for row in A[d + 1 : N - d - 1]])
    queue.extend(A[N - d - 1][d : M - d][::-1])
    queue.extend([row[d] for row in A[d + 1 : N - d - 1]][::-1])
    queue.rotate(-(R % len(queue)))


    for i in range(d, M - d):
        result[d][i] = queue.popleft()
    for i in range(d + 1, N - d - 1):
        result[i][M - d - 1] = queue.popleft()
    for i in range(M - d - 1, d - 1, -1):
        result[N - d - 1][i] = queue.popleft()
    for i in range(N - d - 2, d, -1):
        result[i][d] = queue.popleft()

for line in result:
    print(*line)