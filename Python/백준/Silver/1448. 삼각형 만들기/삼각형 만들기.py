input = __import__('sys').stdin.readline

N = int(input())
lst = sorted([int(input()) for _ in range(N)], reverse=True)

result = -1
for i in range(N - 2):
    if lst[i] < lst[i + 1] + lst[i + 2]:
        result = sum(lst[i:i+3])
        break

print(result)
