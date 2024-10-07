import sys
input = sys.stdin.readline

N = int(input())
lst = [0] * 10001

for _ in range(N):
    lst[int(sys.stdin.readline())] += 1

for i in range(10001):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)