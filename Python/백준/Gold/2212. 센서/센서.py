import sys
input = sys.stdin.readline


def solution():
    if K > N:
        return 0

    dist = []
    for i in range(1, N):
        dist.append(lst[i] - lst[i-1])
    dist.sort()
    for _ in range(K-1):
        dist.pop()
    return sum(dist)


N = int(input())
K = int(input())
lst = sorted(list(map(int, input().split())))

result = solution()
print(result)