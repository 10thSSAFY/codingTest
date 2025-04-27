input = __import__('sys').stdin.readline
from collections import deque


def solution(num):
    L = len(num)
    for i in range(L):
        n = int(num[L - 1 - i], 36)
        lst[n] += (35 - n) * (36 ** i)


def base36(x):
    if x == 0:
        return 0
    q = deque()
    while x:
        q.appendleft('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[x % 36])
        x //= 36
    return "".join(q)


N = int(input())
sum_num = 0
lst = [0] * 36
for _ in range(N):
    S = input().rstrip()
    sum_num += int(S, 36)
    solution(S)

lst.sort(reverse=True)

K = int(input())
for i in range(K):
    sum_num += lst[i]

print(base36(sum_num))
