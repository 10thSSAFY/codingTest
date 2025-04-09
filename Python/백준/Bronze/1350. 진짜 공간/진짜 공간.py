N = int(input())
lst = list(map(int, input().split()))
C = int(input())

result = 0
for i in range(N):
    result += C * (lst[i] // C)
    result += C if lst[i] % C else 0

print(result)