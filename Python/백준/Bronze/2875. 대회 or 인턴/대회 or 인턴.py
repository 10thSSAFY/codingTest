N, M, K = map(int, input().split())

result = 0
while True:
    if N >= 2 and M >=1 and N + M - 3 >= K:
        N -= 2
        M -= 1
        result += 1
    else:
        break

print(result)