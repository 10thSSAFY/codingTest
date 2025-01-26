import sys
input = sys.stdin.readline


n = int(input())
if n == 0:
    print(0)
else:
    lst = []
    for i in range(n):
        lst.append(int(input()))
    lst.sort()

    d = int(n * 0.15 + 0.5)
    result = []

    if d > 0:
        print(int(sum(lst[d:-d]) / len(lst[d:-d]) + 0.5))
    else:
        print(int(sum(lst) / len(lst) + 0.5))
