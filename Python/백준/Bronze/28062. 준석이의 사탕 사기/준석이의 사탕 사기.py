N = int(input())
A = list(map(int, input().split()))

result = 0
odd = 0
min_odd = 1001
for i in range(N):
    num = A[i]
    result += num

    if num % 2 == 1:
        odd = (odd + 1) % 2
        min_odd = min(min_odd, num)

if odd == 1:
    result -= min_odd

print(result)