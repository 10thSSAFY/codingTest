import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    d, n, s, p = map(int, input().split())

    if d + n * p < n * s:
        print("parallelize")
    elif d + n * p > n * s:
        print("do not parallelize")
    else:
        print("does not matter")