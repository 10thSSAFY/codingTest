import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append((y, x))

lst.sort()
for (y, x) in lst:
    print(x, y)