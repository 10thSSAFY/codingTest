N = int(input())

jinju = ''
money = 0
lst = []
for _ in range(N):
    D, C = map(str, input().split())
    lst.append(int(C))
    if D == 'jinju':
        print(C)
        money = int(C)

lst.sort()
print(len(lst) - lst.index(money) - 1 - (lst.count(money) - 1))