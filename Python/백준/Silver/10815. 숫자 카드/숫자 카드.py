import sys
input = sys.stdin.readline

N = int(input())
Nlst = sorted(list(map(int, input().split())))
M = int(input())
Mlst = list(map(int, input().split()))

res = ''
for num in Mlst:
    s, e = 0, N-1
    find = False
    while s <= e:
        mid = (s + e) // 2
        if num < Nlst[mid]:
            e = mid - 1
        elif num > Nlst[mid]:
            s = mid + 1
        else:
            find = True
            break
            
    print(1 if find else 0, end=' ')
