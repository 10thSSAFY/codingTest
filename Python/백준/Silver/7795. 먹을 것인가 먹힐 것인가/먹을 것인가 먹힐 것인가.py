import sys
input = sys.stdin.readline


def search(lst, a):
    s, e = 0, M-1
    res = -1
    while s <= e:
        m = (s + e) // 2
        if lst[m] < a:
            res = m
            s = m + 1
        else:
            e = m - 1
    return res


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt = 0
    for a in A:
        cnt += (search(B, a) + 1)
    print(cnt)

