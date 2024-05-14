import sys
input = sys.stdin.readline


N, M = map(int, input().split())

A_list = []
for _ in range(N):
    A_list.append(int(input()))
A_list.sort()
A_len = len(A_list)

idx_list = {}
for (idx, d) in  enumerate(A_list):
    if d in idx_list:
        continue
    idx_list[d] = idx

for _ in range(M):
    num = int(input())
    if num in idx_list:
        print(idx_list[num])
    else:
        print(-1)