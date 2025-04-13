T = int(input())
lst = [0] * 1000001
for i in range(1000001):
    num = str(i)
    lst[i] = num.count('0')

for _ in range(T):
    N, M = map(int, input().split())
    result = sum(lst[N : M + 1])
    print(result)
