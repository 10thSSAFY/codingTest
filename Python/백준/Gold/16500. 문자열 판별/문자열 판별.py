import sys
input = sys.stdin.readline


def solution(idx):
    global result
    if idx == len(S):
        result = 1
        return

    if dp[idx]:
        return

    dp[idx] = True
    for i in range(N):
        if len(S[idx:]) >= len(A[i]):
            for j in range(len(A[i])):
                if A[i][j] != S[idx + j]:
                    break
            else:
                solution(idx + len(A[i]))
    return


S = input().rstrip()
N = int(input())
A = [input().rstrip() for _ in range(N)]
dp = [False] * 101
result = 0
solution(0)
print(result)