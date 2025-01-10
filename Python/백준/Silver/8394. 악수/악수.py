N = int(input())

a = 1
result = 1
for _ in range(N - 1):
    a, result = result, (a + result) % 10

print(result)