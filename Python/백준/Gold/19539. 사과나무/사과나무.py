N = int(input())
lst = list(map(int, input().split()))

cnt = 0
if sum(lst) % 3 == 0:
    for i in lst:
        cnt += i // 2
    if cnt >= (sum(lst) / 3):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
