def solution(permute_lst):
    curr = 0
    for i in range(len(permute_lst) - 1):
        curr += abs(permute_lst[i] - permute_lst[i + 1])
    return curr


def permutation(depth, permute_lst):
    global result

    if depth == N:
        result = max(result, solution(permute_lst))
        return

    for i in range(N):
        if not bit[i]:
            bit[i] = True
            permutation(depth + 1, permute_lst + [lst[i]])
            bit[i] = False


N = int(input())
lst = list(map(int, input().split()))

bit = [False] * N
result = -float('inf')
permutation(0, [])
print(result)
