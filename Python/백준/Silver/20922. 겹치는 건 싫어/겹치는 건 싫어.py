from collections import defaultdict
import sys
input = sys.stdin.readline


def solution(N, K):
    res = 0
    left, right = 0, 0

    numCnt = defaultdict(int)
    while right < N:
        if numCnt[A[right]] >= K:
            numCnt[A[left]] -= 1
            left += 1
        else:
            numCnt[A[right]] += 1
            right += 1
            res = max(res, right - left)

    return res


N, K = map(int, input().split())
A = list(map(int, input().split()))

result = solution(N, K)
print(result)
