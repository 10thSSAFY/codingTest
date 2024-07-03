import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    lst = list(input().split())
    for l in lst:
        n = len(l)
        for i in range(n-1, -1, -1):
            print(l[i], end='')
        print(' ', end='')
    print()