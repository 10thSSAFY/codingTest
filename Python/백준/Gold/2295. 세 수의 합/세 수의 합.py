import sys
input = sys.stdin.readline


def solution():
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            if lst[i] - lst[j] in sum_set:
                return lst[i]



N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()

sum_set = set()
for X in lst:
    for Y in lst:
        sum_set.add(X + Y)

result = solution()
print(result)
