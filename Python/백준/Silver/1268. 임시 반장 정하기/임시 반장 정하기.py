N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
students = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(5):
        for k in range(N):
            if arr[i][j] == arr[k][j]:
                students[i][k] = 1

result = [0] * N
for i in range(N):
    result[i] = sum(students[i])

for i in range(N):
    if result[i] == max(result):
        print(i + 1)
        break
