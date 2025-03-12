N = int(input())
lst = [int(input()) for _ in range(N)]

time = 30
result = 0
for i in range(N):
    if time >= lst[i]:
        result += 1
    elif time >= (lst[i] + 1) // 2:
        result += 1
    time -= lst[i]
    if time <= 0:
        time = 30

print(result)