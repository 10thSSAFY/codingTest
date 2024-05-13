import sys
input = sys.stdin.readline


N, M = map(int, input().split())

A_list = []
for _ in range(N):
    A_list.append(int(input()))
A_list.sort()
A_len = len(A_list)

for _ in range(M):
    num = int(input())
    s, e, res = 0, A_len - 1, -1
    while s <= e:
        m = (s + e) // 2
        if num == A_list[m]:
            res = m
            e = m - 1
        elif num < A_list[m]:
            e = m - 1
        elif A_list[m] < num:
            s = m + 1
    print(res)