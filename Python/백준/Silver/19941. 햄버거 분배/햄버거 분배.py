N, K = map(int, input().split())
lst = list(input())

result = 0
for i in range(N):
    if lst[i] == 'P':
        for j in range(max(i - K, 0), min(i + K + 1, N)):
            if lst[j] == 'H':
                lst[j] = 'X'
                result += 1
                break

print(result)