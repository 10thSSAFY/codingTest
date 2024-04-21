import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

sub_lst = []
for i in range(1, N):
    sub_lst.append(lst[i] - lst[i-1])

sub_lst.sort(reverse=True)
print(sum(sub_lst[K-1:]))