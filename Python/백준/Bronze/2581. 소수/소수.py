M = int(input())
N = int(input())

lst = []
for i in range(M, N+1):
    e = 0
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                e += 1
                break
        if e == 0:
            lst.append(i)

if len(lst) < 1:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))