N = int(input())
result = 0
for num in range(1, N+1):
    result += num * (N // num)

print(result)