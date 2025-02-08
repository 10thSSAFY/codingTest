import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort(reverse=True)

for num in lst:
    print(num)
