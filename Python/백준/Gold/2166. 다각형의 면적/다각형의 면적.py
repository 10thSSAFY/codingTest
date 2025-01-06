N = int(input())

lst = []
for _ in range(N):
    lst.append(tuple(map(int, input().split(' '))))
lst.append(lst[0])

result = 0
for i in range(N):
    result += lst[i][0] * lst[i + 1][1] - lst[i + 1][0] * lst[i][1]

print(abs(result)/2)