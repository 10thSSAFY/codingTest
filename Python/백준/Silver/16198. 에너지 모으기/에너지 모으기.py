input = __import__('sys').stdin.readline


def solution(n):
    global result

    if len(W) == 2:
        result = max(result, n)
        return

    for i in range(1, len(W) - 1):
        sum_n = W[i - 1] * W[i + 1]

        tmp = W.pop(i)
        solution(n + sum_n)
        W.insert(i, tmp)


N = int(input())
W = list(map(int, input().split()))
result = 0
solution(0)
print(result)